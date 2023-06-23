#  BSD 3-Clause License
#
#  Copyright (c) 2023, Trixter GmbH
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its
#     contributors may be used to endorse or promote products derived from
#     this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import dbm
import contextlib
import json
import warnings
import inspect
import importlib

import ftrack_api

from ftrack_api.symbol import NOT_SET

from ftrack_api.cache import (
    SerialisedCache,
    FileCache
)
from ftrack_api.operation import (
    CreateEntityOperation,
    UpdateEntityOperation,
    Operations
)

from .entities.relationships_parser import RelationshipsParser


_PARSED_RELATIONSHIPS_CACHE = {}


class Session(object):
    """ Delegates all attributes and methods to the ftrack session instance

    Allows us to have our own Session interface for enhanced interaction.
    """

    # exclude members that we don't want to delegate
    MEMBERS = [
        "_session",
        "_session_arguments",
        "_terminated_queries",  # this is our terminated query cache
        "reuse_query_results",
    ]

    def __init__(self, auto_populate=False, auto_connect_event_hub=False, **kwargs):
        # Collect arguments to hand over to the native ftrack_api.Session
        local_args = dict(locals())
        valid_args = [_ for _ in inspect.getfullargspec(ftrack_api.Session.__init__).args if _ not in ('self', 'kwargs')]
        session_arguments = {}
        for arg_key, arg_val in local_args.items():
            if arg_key in valid_args:
                session_arguments[arg_key] = arg_val
        session_arguments.update(kwargs)

        self._session = ftrack_api.Session(**session_arguments)

        # monkey patch ftrack session to find the way back from it to here
        self._session.delegate = self
        self._session_arguments = session_arguments
        self._terminated_queries = {}

        self.reuse_query_results = kwargs.get("reuse_query_results", False)

    def __eq__(self, other):
        if isinstance(other, ftrack_api.Session):
            return other == self._session
        elif isinstance(other, Session):
            return other._session == self._session
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def parsed_relationships(self):
        if not self._session.server_url in _PARSED_RELATIONSHIPS_CACHE:
            relationship_parser = RelationshipsParser(ftrack_session=self._session)
            # types such as "Context" are ambiguous and cannot be used to extract direct relationships
            # example structure - Seq -> Folder -> Shot
            # in this case, establishing a relationship from Seq to Shot is impossible as would any other
            # that went through "parent" or "children" for example
            relationship_parser.exclude_types = {"Context"}
            relationship_parser.parse_session_schemas()
            # attributes that group things cannot be used to extract relationships
            # as an example, "descendants" lists all children and children of children and so on,
            # so they are all flattened with their relationships removed
            relationship_parser.attributes_blacklist = {"descendants", "ancestors", "status_changes"}
            relationship_parser.extract_all_entity_relations()
            _PARSED_RELATIONSHIPS_CACHE[self._session.server_url] = relationship_parser

        return _PARSED_RELATIONSHIPS_CACHE[self._session.server_url]

    def get_cached_collections(self):
        typenames = sorted([str(k) for k, v in self._build_entity_type_classes(self.schemas).items()])
        type_module = importlib.import_module("..entities", __name__)

        type_map = {}
        for name in typenames:
            collection = getattr(type_module, "EntityCollection")
            _type = getattr(type_module, name)
            if _type and issubclass(_type, getattr(type_module, "Entity")):
                cached_entities = [
                    _type.from_entity_type(name=_type.__name__, ftrack_entity=_) for _ in self._local_cache.values()
                    if _.__class__.__name__ == name
                ]
                entitycollection = collection._make_empty(_type, self)
                type_map[_type] = entitycollection.from_entities(cached_entities)

        return type_map

    def reconnect(self, **kwargs):
        """ Closes the active session and connects a new session with the
        option to update session arguments.

        Args:
            kwargs: optional overrides for existing session arguments.
        """
        session_attributes = {}
        valid_args = [_ for _ in inspect.getfullargspec(ftrack_api.Session.__init__).args if _ not in ('self', 'kwargs')]
        for arg in valid_args:
            if hasattr(self._session, arg):
                session_attributes[arg] = getattr(self._session, arg)

        self._session.close()
        self._session_arguments.update(session_attributes)
        self._session_arguments.update(kwargs)
        self._session = ftrack_api.Session(**self._session_arguments)
        # Some of the attributes propagated as arguments are cache-related, therefore we
        # need to clear the cache in order to make sure it's empty for the new session.
        self._session.cache.clear()

        self._terminated_queries = {}

    def close(self):
        """Closes the session"""
        self._session.close()
        self._terminated_queries = {}

    def reconnect_and_commit(self, initial_operations_path, **kwargs):
        """
        Given a path to a dumped database [.dbm] this method will apply
        the stored operations to the database.

        The session is reconnected to start from a clean cache and
        an empty operations stack. Then the local cache and operations
        will be updated with the contents of the dumped cache.
        To sync the ftrack database with the local cache a commit is
        issued.

        Args:
            initial_operations_path ():
            kwargs: optional overrides for existing session arguments.

        Returns:

        """
        self.reconnect(**kwargs)

        operations = Operations()

        try:
            _db = dbm.open(initial_operations_path, "r")
            _db.close()
        except dbm.error:
            raise OSError("Unable to open Database `{}`".format(initial_operations_path))

        initial_cache = SerialisedCache(
            FileCache(initial_operations_path),
            encode=self._session.encode,
            decode=self._session.decode
        )
        for key in initial_cache.keys():
            if key == "__operations__":
                initial_operations = json.loads(initial_cache.get(key))

                for op in initial_operations:
                    if op["operation"] == "create":
                        del op["operation"]
                        operation = CreateEntityOperation(**op)
                    elif op["operation"] == "update":
                        if op["old_value"] in initial_cache.keys():
                            op["old_value"] = initial_cache.get(str(op["old_value"]))
                            if op["old_value"] == "NOT SET":
                                op["old_value"] = NOT_SET
                        if op["new_value"] in initial_cache.keys():
                            op["new_value"] = initial_cache.get(str(op["new_value"]))
                            if op["new_value"] == "NOT SET":
                                op["new_value"] = NOT_SET
                        del op["operation"]
                        operation = UpdateEntityOperation(**op)
                    else:
                        raise KeyError("Unknown Operation `{}`.".format(op["operation"]))

                    operations.push(operation)
            else:
                self._local_cache.set(key, initial_cache.get(key))

        self._session.recorded_operations = operations
        self._session.commit()

    @staticmethod
    def _serialise_value(value):
        if value == NOT_SET:
            return "NOT SET"
        elif hasattr(value, "entity_type"):
            return "('{}', ['{}'])".format(
                value.entity_type,
                value["id"]
            )
        else:
            return value

    @contextlib.contextmanager
    def reusing_query_results(self):
        """Temporarily enable query cache"""
        backup = self.reuse_query_results
        self.reuse_query_results = True
        try:
            yield
        finally:
            self.reuse_query_results = backup
            
    @contextlib.contextmanager
    def deferred_operations(self, filepath, clear=True):

        file_cache = FileCache(filepath)
        serialised_cache = SerialisedCache(
            file_cache,
            encode=self.encode,
            decode=self.decode
        )

        if clear:
            serialised_cache.clear()

        # add the filecache temporarily
        self.cache.caches.append(serialised_cache)
        cache_index = len(self.cache.caches) - 1

        # store all previously recorded operations
        _previous_operations = self.recorded_operations

        # clear operations temporarily
        deferred = Operations()
        self.recorded_operations = deferred

        yield

        # sync cache
        with file_cache._database() as database:
            for key, value in database.items():
                entity_data = json.loads(value)
                for attr, attr_value in entity_data.items():
                    if isinstance(attr_value, dict):
                        entity_type = attr_value.get("__entity_type__")
                        if entity_type:
                            # if this is an entity we check whether the linked entity is available
                            # in our filecache
                            # TODO: eventually we should check for the actual primary key here
                            #  for our current usecase it seems ok to blindly use the id
                            cache_key = "('{}', ['{}'])".format(entity_type, attr_value["id"])
                            if cache_key not in serialised_cache.keys():
                                serialised_cache.set(cache_key, self._local_cache.get(cache_key))

            # serialise operations and store them in the database
            ops = []
            for op in self.recorded_operations:
                if isinstance(op, CreateEntityOperation):
                    ops.append(
                        {
                            "operation": "create",
                            "entity_data": op.entity_data,
                            "entity_type": op.entity_type,
                            "entity_key": op.entity_key
                        }
                    )
                elif isinstance(op, UpdateEntityOperation):
                    ops.append(
                        {
                            "operation": "update",
                            "entity_type": op.entity_type,
                            "entity_key": op.entity_key,
                            "attribute_name": op.attribute_name,
                            "old_value": self._serialise_value(op.old_value),
                            "new_value": self._serialise_value(op.new_value)
                        }
                    )

            serialised_cache.set("__operations__", json.dumps(ops))

        # remove temporary filecache
        self.cache.caches.pop()

        # load previous operations back in the stack
        self.recorded_operations = _previous_operations

    def __getattribute__(self, item):
        # delegating access to those attributes is neccessary to support the
        # temporary attribute value decorator
        if item in ("__dict__", "__slots__"):
            return self.__getattr__(item)
        else:
            return super(Session, self).__getattribute__(item)

    def __getattr__(self, key):
        if hasattr(self._session, key):
            return getattr(self._session, key)
        else:
            raise AttributeError("Attribute '{}' does not exist.".format(key))

    def __setattr__(self, key, value):
        if key in self.MEMBERS:
            super(Session, self).__setattr__(key, value)
            setattr(self._session, key, value)
        elif hasattr(self, key):
            setattr(self._session, key, value)
        else:
            raise AttributeError("Attribute '{}' does not exist.".format(key))

    def __delattr__(self, item):
        if item in self.MEMBERS:
            super(Session, self).__delattr__(item)
            delattr(self._session, item)
        elif hasattr(self, item):
            delattr(self._session, item)
        else:
            raise AttributeError("Attribute '{}' does not exist.".format(item))


class _SessionDelegate(Session):
    def __init__(self, *args, **kwargs):
        warnings.warn('"_SessionDelegate" class got renamed to "Session"',
                      DeprecationWarning)
        super(_SessionDelegate, self).__init__(*args, **kwargs)


# main session
# TODO: defer connection
SESSION = Session()
SESSION.auto_populate = False
