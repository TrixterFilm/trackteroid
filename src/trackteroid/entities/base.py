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

import inspect
import importlib
import logging
import re
from collections import (
    OrderedDict,
    defaultdict,
    namedtuple,
)
from copy import copy
import sys

from ftrack_api.symbol import NOT_SET

from .declarations import *

from .schematypes import (
    CUSTOM_ATTRIBUTE_TYPE_COMPATIBILITY,
    AttributeInfo
)
from ..query import (
    Criterion,
    Criteria,
    utils
)
from ..configuration import (
    LOGGING_NAMESPACE,
    ALLOWED_FOR_DELETION_RESOLVER,
    WARN_ON_INJECT
)


LOG = logging.getLogger("{}.entities".format(LOGGING_NAMESPACE))

_RELATIONSHIPS_CACHE = {}


def TargetRelation(relation="", collection=False):
    """TargetRelation function that "looks" like a class (due to its CamelCase naming on purpose)"""
    return namedtuple(TargetRelation.__name__, ['relation', 'collection'])(relation, collection)


class Relationship(dict):
    """ A simple helper class to check for equality
    """
    parent = None

    def __init__(self):
        super(Relationship, self).__init__()

        self._entity_type_name = None
        self.session = None
        self.schema = None

        try:
            self._entity_type_name = inspect.stack()[1][3]
        except IndexError:
            LOG.warning("Unable to identify Entity Type.", exc_info=True)

    def _infer_from_session_schema(self, session):
        def _to_class(classname):
            return getattr(sys.modules[__name__], classname, None)

        # TODO: check for actual available types
        if self._entity_type_name and self._entity_type_name != "_EntityBase":
            entity_data = session.parsed_relationships.relationships.get(self._entity_type_name)
            if entity_data:
                LOG.debug("Inferring relationship data for {}".format(self._entity_type_name))

                for entity, relation in entity_data.get("non_collection").items():
                    self.add(_to_class(entity), ".".join(relation))
                for entity, relation in entity_data.get("collection").items():
                    self.add(_to_class(entity), ".".join(relation), collection=True)
            else:
                LOG.warning("Couldn't find entry for '{}' in relationships cache.".format(self._entity_type_name))

    @property
    def _cache_key(self):
        server_url, schema_name, entity_type_name = None, None, None
        try:
            server_url = self.session.server_url
            schema_name = self.schema["name"]
            entity_type_name = self._entity_type_name
        except (AttributeError, KeyError):
            pass

        return server_url, schema_name, entity_type_name

    @property
    def global_cache(self):
        return _RELATIONSHIPS_CACHE

    def __repr__(self):
        return str(self)

    def __str__(self):
        key = self._cache_key
        return str(_RELATIONSHIPS_CACHE.get(key, {}))

    def _validate_access(self):
        _error_msg_template = "No {} was set for the current Relationship object. " \
            "Relationship needs to be called with session and schema instance before " \
            "relations can be retrieved."

        # as we do have to read from a global cache we need to assume a session and schema have been defined
        # for our current instance so we can look up previously parsed relationship information from the global
        # cache
        if self.session is None:
            raise AssertionError(_error_msg_template.format("session"))
        if self.schema is None:
            raise AssertionError(_error_msg_template.format("schema"))

    def __getitem__(self, item):
        self._validate_access()

        from_cache = _RELATIONSHIPS_CACHE.get(self._cache_key, {})

        for key, value in from_cache.items():
            if key and (key == item):
                return value
        return super(Relationship, self).__getitem__(item)

    def __setitem__(self, item, value):
        self._validate_access()
        key = self._cache_key

        from_cache = _RELATIONSHIPS_CACHE.get(key, {})
        if not from_cache:
            _RELATIONSHIPS_CACHE[key] = from_cache
        from_cache[item] = value

    def __call__(self, session, schema, entity_type=None):
        # TODO: how to deal with race condition in case queries will run in threads for the same server/session

        # whenever being called store the information about the used session and used schema
        self.session = session
        self.schema = schema
        if entity_type:
            self._entity_type_name = entity_type.__name__

        # build a key for the cached based on used schema name and session server url
        key = self._cache_key

        # on initial request infer all relationships from database and custom schema
        if key not in _RELATIONSHIPS_CACHE:
            # always do a copy of ourselves that will be added to the cache as a Relationship instance
            # is currently being used as a class attribute
            self._infer_from_session_schema(session)

            # TODO: warn if schema doesn't have entities set
            collection_attributes = session.parsed_relationships.array_attributes
            for target_entity_name, relation in schema.get("entities", {}).get(self._entity_type_name, {}).items():
                collection = None

                if not isinstance(relation, list):
                    _relation = [relation]
                else:
                    _relation = relation

                for some_relation in _relation:
                    attribute_tokens = some_relation.split(".")
                    leaf_attribute = some_relation.split(".")[-1]

                    if len(attribute_tokens) > 1:
                        _collection = leaf_attribute in collection_attributes
                    else:
                        _collection = bool(re.match(r"^(children|ancestors)(\[\w+\])?", attribute_tokens[0]))

                    if collection is None:
                        collection = _collection
                    if collection != _collection:
                        raise AttributeError(
                            "Given relationships '{}' attribute array state is ambigious.".format(
                                relation
                            )
                        )

                self.add(globals()[target_entity_name], relation, collection)

    def add(self, target, relation, collection=False):
        """ Adds a new relationship
        """
        self[target] = TargetRelation(relation, collection)

    def get(self, item, default=None):
        try:
            return self[item]
        except KeyError:
            return default


class EmptyCollection(object):
    """ Special collection which is used instead of an EntityColleciton with
    zero Entities. This acts as an Opiontal which will forward any attribute
    getters by always returning itself. This reduces the need for constant
    conditional checks (null checks) and makes the code simpler
    """
    __slots__ = ["_entity", "depth", "source", "_current_iter_index", "_session"]

    def __init__(self, _type=None, source=None, depth=1, session=None):
        self._entity = _type
        self.depth = depth
        self.source = source
        self._current_iter_index = 0
        self._session = session

    def __call__(self, *args, **kwargs):
        return self

    def __contains__(self, item):
        return False

    def __copy__(self):
        return EmptyCollection(
            _type=self._entity,
            depth=self.depth + 1,
            source=self.source,
            session=self._session
        )

    def __eq__(self, other):
        equal = False
        if isinstance(other, EmptyCollection):
            equal = True
            for slot in EmptyCollection.__slots__:
                equal = equal and getattr(self, slot) == getattr(other, slot)
        return equal

    def __getattr__(self, item):
        current_depth = self.depth
        collection_copy = copy(self)
        # in case we use methods like .values() or .from_entities() etc
        # we need to take care to not increment the depth, as it doesn represent
        # an attribute/relation access
        if item in [_ for _ in dir(EntityCollection) if not re.match(r"__\w+__|children", _)]:
            collection_copy.depth = current_depth
        return collection_copy

    def __getitem__(self, item):
        # TEST: Maybe we should return somthing else when accessing POD
        #  attributes so we can avoid doing this:
        #  names.append(Query(Asset).by_name("test").get_all().name or [])

        if inspect.isclass(item) and issubclass(item, Entity):
            self._entity = item()

        return self

    def __iter__(self):
        self._current_iter_index = 0
        return self

    def __len__(self):
        return 0

    def __next__(self):
        if self._current_iter_index == 0:
            self._current_iter_index += 1
            return copy(self)
        else:
            raise StopIteration

    # python 2 compatibility
    def next(self):
        return self.__next__()

    def __nonzero__(self):
        return False

    def __repr__(self):
        return "EmptyCollection[{}]".format(self._entity)

    @property
    def entity_type(self):
        return self._entity

    def create(self, **kwargs):
        assert self.depth == 1, \
            """
            This attribute does not exist yet. The parent attribute also did not exist.
            Create can only be called on existing attributes OR if at least the parent
            exists.
            """
        entitycollection = EntityCollection._make_empty(self._entity.__class__, self._session)
        return entitycollection.create(empty=self, **kwargs)

    def create_batch(self, *attributes):
        """

        Args:
            *attribute ():

        Returns:

        """

        collections = []

        for _attributes in attributes:
            collections.append(self.create(**_attributes))

        return EmptyCollection(_type=self._entity).union(*collections)

    def union(self, *collections):
        if len(collections) == 1:
            return collections[0]
        
        first = collections[0]
        others = [_ for _ in collections[1:] if _]
        first_type = first.entity_type
        for other_type in (_.entity_type for _ in others if _):
            assert first_type == other_type, "Can't union collections with different types. {} != {}."\
                .format(first_type, other_type)
        
        return first.union(*others)


class EntityCollection(object):
    """ An immutable sorted set of unique Entities of the same entity type.
    """
    MEMBERS = [
        "_entity",
        "_entities",
        "_query",
        "query",
        "_schema_types_map",
        "_current_iter_index",
        "_session",
        "_source"
    ]

    def __init__(self, _cls=None, entities={}, session=None):
        super(EntityCollection, self).__init__()
        self._entity = _cls()

        self._entities = entities
        self._query = None
        self._current_iter_index = []
        self._session = session

        # similar to the source attribute on EmptyCollection
        # we sometimes need to keep track of what produced this
        # current collection
        self._source = (None, None)

        self._schema_types_map = {
            "string": (str,),
            "number": (float,),
            "boolean": (bool,),
            "integer": (int,),
            "mapped_array": (dict,)
        }

    def __contains__(self, other):
        if isinstance(other, str):
            return other in self.keys()
        elif isinstance(other, Entity):
            return other in self.values()
        elif isinstance(other, EntityCollection):
            return all([_ in self.keys() for _ in other.keys()])

    def __eq__(self, other):
        if isinstance(other, EntityCollection):
            return [_.ftrack_entity for _ in self.values()] == \
                   [_.ftrack_entity for _ in other.values()]
        else:
            return False

    def __getattr__(self, item):
        # TODO: clean after we have tests for this functionality
        if self and item in list(self.values())[0].ftrack_entity.keys():
            entities = []
            values = []
            entity_type = None
            for entity in self.values():
                value = entity[item]
                # resolve entities in collections
                if value.__class__.__name__ == "Collection":
                    for _ in value:
                        # wrap ftrack entity
                        if hasattr(_, "entity_type"):
                            entities.append(Entity.from_entity_type(str(_.entity_type), ftrack_entity=_))
                        else:
                            values.append(_)
                    if not entities and not values and not entity_type:
                        entity_type = Entity.from_entity_type(
                            name=self._get_attribute_compatibility_types(item).types[0].__name__
                        )
                elif value.__class__.__name__ == "KeyValueMappedCollectionProxy":
                    values.append(dict(entity.ftrack_entity["metadata"].items()))

                # wrap ftrack entity
                elif hasattr(value, "entity_type"):
                    entities.append(Entity.from_entity_type(str(value.entity_type), ftrack_entity=value))
                else:
                    values.append(value)

            if entities:
                return self.from_entities(entities, source=(item, self))
            elif entity_type:
                return EmptyCollection(_type=entity_type, source=self, session=self._session)
            return values

        elif item == "get":
            return self._get_relatives

        # handle custom attributes
        elif item.startswith("custom_"):
            attr = item.replace("custom_", "")
            values = []
            for entity in self.values():
                values.append(entity.ftrack_entity["custom_attributes"].get(attr))
            return values

        # handle collection.<type>
        elif item in globals():
            # if not already parsed and cached let's do it now
            self._entity.relationship(
                session=self.query.session,
                schema=self.query.schema,
                entity_type=self._entity.__class__
            )
            if self._entity.relationship.get(globals()[item]):
                relation = self._entity.relationship.get(globals()[item]).relation

                result = None

                if not isinstance(relation, list):
                    relation = [relation]

                for some_relation in relation:
                    current = None
                    # tokenize the attribute chain
                    for token in some_relation.split("."):
                        _filter = None
                        # and also identify filters like with `parent[Shot]`
                        _ = re.findall(r"\w+", token)
                        if len(_) == 2:
                            token, _filter = _
                        elif len(_) > 2:
                            raise ValueError("Unable to identify attribute and filter within token '{}'.".format(_))

                        _collection = self if current is None else current
                        current = getattr(_collection, token)

                        if NOT_SET in current:
                            self._entity.log.warning(
                                "Was the attribute you're trying to access projected? "
                                "A symbol.NOT_SET found on '{}' access. This would resolve to '{}'.".format(
                                    item,
                                    ", ".join(relation)
                                )
                            )

                        # TODO: check if the entity we need for filtering is in the globals
                        if _filter:
                            current = current[globals()[_filter]]

                    if result is None:
                        result = current
                    else:
                        result = result.union(current)

                return result

        else:
            raise AttributeError("Attribute {} does not exist.".format(item))

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            # no one needs to know that internally we store the id as the key!
            return self.from_entities(list(self.values())[item])
        elif isinstance(item, str):
            return self.from_entities(self._entities[item])
        elif issubclass(item, Entity):
            return self.resolve_subtype(item)
        # TODO: would there be a scenarios outside our __getattr__ usecase
        #  where this would be a direct ForwardDeclaration subclass?
        elif issubclass(item, ForwardDeclaration):
            return self.resolve_subtype(item)

    def __hash__(self):
        return hash(tuple(self.keys()))

    def __iter__(self):
        self._current_iter_index.append(0)
        return self

    def __len__(self):
        return len(self.keys())

    # TODO: how to cleanup if we have a break statement?
    def __next__(self):
        if self._current_iter_index[-1] >= len(self.keys()):
            del self._current_iter_index[-1]
            raise StopIteration
        else:
            self._current_iter_index[-1] += 1
            return self[self._current_iter_index[-1] - 1]

    # python 2 compatibility
    def next(self):
        return self.__next__()

    def __repr__(self):
        """ Formats self like EntityCollection[EntityType]{NumberOfEntities}.

        Example:
            EntityType[AssetVersion]{23}

        Returns:
            str: Formatted string representing the EntityCollection.
        """
        return "{}[{}]{{{}}}".format(self.__class__.__name__, self._entity, len(self))

    def __setattr__(self, key, value):
        # TODO: setting uses_versions and used_in_versions will not update bidirectionally
        #  Can we solve this in a generic way?
        # should we update this so we have the correct data locally?
        if key in self.MEMBERS:
            super(EntityCollection, self).__setattr__(key, value)
        else:
            attribute_value = getattr(self, key, None)
            if attribute_value is not None:
                # If the attribute access produces a collection
                # we potentially can not go by key as the attribute
                # access can be a type based shortcut.
                # Therefore we need to resolve the collections produced
                # via the full attribute chain and retain the last attribute
                # as our key.
                if not isinstance(attribute_value, list):
                    key, collection = attribute_value._source
                else:
                    collection = self

                compatible, reason = collection._is_attribute_compatible_with_value(key, value)
                if not compatible:
                    raise TypeError(reason)

                if isinstance(value, (list, tuple, EntityCollection)) \
                        and len(collection) == 1 \
                        and list(collection._entities.values())[0].ftrack_entity[key].__class__.__name__ == "Collection":
                    if isinstance(value, EntityCollection):
                        list(collection.values())[0].ftrack_entity[key] = [_.ftrack_entity for _ in value.values()]
                else:
                    for idx, entity in enumerate(collection.values()):
                        if key.startswith("custom_"):
                            if isinstance(value, (list, tuple, EntityCollection)):
                                entity.ftrack_entity["custom_attributes"][key.replace("custom_", "")] = value[idx]
                            else:
                                entity.ftrack_entity["custom_attributes"][key.replace("custom_", "")] = value
                        elif entity.ftrack_entity[key].__class__.__name__ == "KeyValueMappedCollectionProxy":
                            _should_capture = False
                            if isinstance(value, (list, tuple)):
                                if any(_ not in  value[idx].keys() for _ in entity.ftrack_entity[key]):
                                    _should_capture = True
                                for _key, _value in value[idx].items():
                                    entity.ftrack_entity[key][_key] = _value
                            else:
                                if not len(value):
                                    entity.ftrack_entity[key] = value
                                else:
                                    for _key, _value in value.items():
                                        entity.ftrack_entity[key][_key] = _value
                        else:
                            if isinstance(value, EntityCollection):
                                entity.ftrack_entity[key] = list(value.values())[idx].ftrack_entity
                            elif isinstance(value, (list, tuple)):
                                entity.ftrack_entity[key] = value[idx]
                            else:
                                entity.ftrack_entity[key] = value

            else:
                raise AttributeError("Attribute {} does not exist.".format(key))

    def __nonzero__(self):
        return len(self) > 0

    def _init_type_map(self, type_def):
        """ builds a dictionary with EmptyCollections, based on the given type definitions

        Notes:
              This is primarily useful for resolving TypedContext subclasses
        Args:
            type_def (TypesBase subclass): availavle types from schema

        Returns:
            dict where the key is the available type and the value and EmptyCollection of the same type
        """
        # Initialize the dictionary with EmptyCollections of correct type so
        # we can create TypedContexts for object_types that have not been
        # created in the pertinent context
        type_map = {}
        for _type in type_def.types:
            empty = EmptyCollection(
                _type=Entity.from_entity_type(str(_type)),
                source=self,
                session=self._session
            )
            type_map[_type] = empty
        return type_map

    def resolve_subtype(self, entity_type):
        """ filters entities by matching the entity_type returns a collection of the given type including the matches

        Args:
            entity_type (Entity): a given entity class that must be a subclass of the type of the current collection

        Returns:
            EntityCollection[entity_type] or EmptyCollection[entity_type]
        """
        if not issubclass(entity_type, ForwardDeclaration):
            # this can only work if the given entity type is a subclass of our currently
            # used collection type, like TypedContext -> AssetBuild|Shot|Sequence... or Component -> FileComponent
            # TODO: re-think the necessity of checking for the actual base type
            #  Enforcing a type coercion before filtering via entity type makes the code more clear, but is
            #  not strictly needed for correct filtering.
            assert issubclass(entity_type, self.entity_type)
        else:
            entity_type = getattr(importlib.import_module("..entities", __name__), entity_type.__name__)

        matched_types = self.filter(lambda x: list(x.values())[0].ftrack_entity.entity_type == entity_type.__name__)
        return self.from_entities(
            [
                Entity.from_entity_type(entity_type.__name__, ftrack_entity=_.ftrack_entity) for _ in
                matched_types.values() or []  # fall back to empty list in case we already have an EmptyCollection
            ],
            type_override=entity_type,
            source=getattr(matched_types, "source", None)
        )

    @property
    def children(self):
        """ get all children

        Returns:
            EntityCollection[TypedContext]
        """
        # TODO: deal with this when it becomes a problem ;)
        #  Other entities like Context or Group have children too. When we need to
        #  access those we have to implement the functionality properly here.
        # if not isinstance(self._entity, TypedContext):
        #     getattr(self, "children")

        default_projections = ["children.{}".format(_) for _ in self._entity.projections]
        self._simple_children_fetch("children.object_type.name", *default_projections)

        children_entities = []

        for entity in self.values():
            if entity["children"]:
                for child in entity["children"]:
                    children_entities.append(
                        Entity.from_entity_type("TypedContext", ftrack_entity=child)
                    )

        return self.from_entities(children_entities, source=self)

    def query_children(self, projections=None, session=None):
        """Queries and returns the children of the collection. Only supported for
        entities that have a "children" relation

        Args:
            projections (`list` of `str`): Projections to fetch from the children
            session (Session): Optional session to use.

        """
        projections_ = ["children.{}".format(_) for _ in self._entity.projections]
        projections_ += ["children.{}".format(x) for x in (projections or [])]
        projections_.append("children.object_type.name")
        query = self.as_query(use_ids=True)
        query.projections = list(set(projections_).union(query.projections))  # update not override
        return query.get_all(session=session or self._session).children

    # TODO: move to avoid circular import
    @staticmethod
    def _make_empty(entity_class, session):
        # UGLY AS HELL!!!!!
        entitycollection = EntityCollection(_cls=entity_class, entities=OrderedDict())
        # this special import is neccessary to avoid a circular import
        adhoc_type = getattr(importlib.import_module("...query", __name__), "Query")
        entitycollection.query = adhoc_type(entity=entity_class, session=session)
        entitycollection.query.valid = False
        entitycollection._session = session
        return entitycollection

    @property
    def entity_type(self):
        return self._entity.__class__

    def link_inputs(self, collection):
        """ Links compatible Entities as inputs to the current collection.

        Args:
            collection (EntityCollection): Collection of entities to link as inputs

        Returns:
            self
        """
        self.fetch_attributes("incoming_links.from_id")
        if len(collection) != 0:
            for entity in self:
                links = entity.incoming_links
                for _id in collection.id:
                    if _id not in links.from_id:
                        entity.incoming_links.create(from_id=_id, to_id=entity.id[0])
        else:
            LOG.warning("The collection you want to link is empty.")

        return self

    def link_outputs(self, collection):
        """ Links compatible Entities as outputs to the current collection.

        Args:
            collection (EntityCollection): Collection of entities to link as outputs

        Returns:
            self
        """
        self.fetch_attributes("outgoing_links.to_id")
        if len(collection) != 0:
            for entity in self:
                links = entity.outgoing_links
                for _id in collection.id:
                    if _id not in links.to_id:
                        entity.outgoing_links.create(from_id=entity.id[0], to_id=_id)
        else:
            LOG.warning("The collection you want to link is empty.")

        return self

    def unlink_inputs(self, collection):
        """ Deletes all incoming links between collection and self.

        Args:
            collection (EntityCollection): Collection of entities to unlink as inputs

        Returns:
            EntityColleciton of remaining input entities.
        """
        self.fetch_attributes("incoming_links.from_id")
        if len(collection) != 0:
            for entity in self:
                links = entity.incoming_links
                for _id in collection.id:
                    links.filter(lambda x: str(_id) == str(x.from_id[0])).delete()
        else:
            LOG.warning("The collection you want to unlink is empty.")

        return self

    def unlink_outputs(self, collection):
        """ Deletes all outgoing links between self and collection.

        Args:
            collection (EntityCollection): Collection of entities to unlink as outputs.

        Returns:
            EntityColleciton of remaining output entities.
        """
        self.fetch_attributes("outgoing_links.to_id")
        if len(collection) != 0:
            for entity in self:
                links = entity.outgoing_links
                for _id in collection.id:
                    links.filter(lambda x: str(_id) == str(x.to_id[0])).delete()
        else:
            LOG.warning("The collection you want to unlink is empty.")

        return self

    def _is_attribute_compatible_with_value(self, attribute_name, value):
        attribute_info = self._get_attribute_compatibility_types(attribute_name)
        value_info = self._get_value_type(value)
        compatible, reason = True, ""

        # TODO: make sure we compare the actual types and not just the names
        # TEST: What happens if we naively do this. Adjust unittests to check!
        if value_info.types not in [_ for _ in attribute_info.types]:
            compatible, reason = False, \
                (
                    "The given value '{}' does not have the correct type "
                    "for the receiver attribute '{}'. {} != {}".format(
                        value,
                        attribute_name,
                        value_info.types,
                        attribute_info.types
                    )
                )
            return compatible, reason

        if isinstance(value, (EntityCollection, tuple, list)):
            _reason = (
                "When setting an attribute on a receiver collection, "
                "we expect the given value to have the same amount of elements as our collection has entities "
                "or in case it is an iterable to have the same length."
            )
            if attribute_info.array:
                if len(self) > 1:
                    # we want to assign a value to multiple entities
                    if len(self) != len(value):
                        compatible, reason = False, _reason
            elif len(self) != len(value):
                compatible, reason = False, _reason
        elif len(self) > 1:
            # value is not a Collection/Array, but we contain multiple entities
            compatible, reason = False, \
                "The given value is not a collection or array, but the receiver contains more than a single entity."

        return compatible, reason

    @staticmethod
    def _get_value_type(value):
        if isinstance(value, (EntityCollection, EmptyCollection)):
            return AttributeInfo(
                types=type(value._entity),
                array=True
            )
        elif isinstance(value, (tuple, list)):
            return AttributeInfo(
                types=type(value[0]),
                array=True
            )
        else:
            return AttributeInfo(types=type(value))

    def _get_attribute_compatibility_types(self, attribute_name):
        """ Returns an AttributeInfo object that encodes which values can
        potentially be assigned to self.[attribute_name]
            Args:
                 attribute_name (str): The name of the attribute we want to check.

            Returns:
                AttributeInfo: An AttributeInfo object that encodes the values that
                self.[attribute_name] can consume.
        """
        if attribute_name.startswith("custom_"):
            attribute_name = attribute_name.replace("custom_", "")
            attribute_info = getattr(CUSTOM_ATTRIBUTE_TYPE_COMPATIBILITY, attribute_name)
            return attribute_info

        entity_schema = None

        for schema in self._session.schemas:
            if schema["id"] == self._entity.__class__.__name__:
                entity_schema = schema

        property_schema = entity_schema["properties"][attribute_name]

        attribute_info = AttributeInfo()

        if property_schema.get("$ref"):
            attribute_info.types = (globals()[property_schema["$ref"]],)
        elif property_schema.get("key_value_attributes"):
            attribute_info.types = self._schema_types_map[property_schema["type"]]
        elif property_schema.get("items"):
            attribute_info.array = True
            attribute_info.types = (globals()[property_schema["items"]["$ref"]],)
        elif property_schema.get("type"):
            attribute_info.types = self._schema_types_map[property_schema["type"]]
        else:
            raise AttributeError("Attribute '{}' not found in schema '{}'.".format(attribute_name, entity_schema["id"]))

        return attribute_info

    def keys(self):
        return self._entities.keys()

    def values(self):
        return self._entities.values()

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, instance):
        """ Sets the query to a copy of the given query instance.
        """
        self._query = copy(instance)

    def from_entities(self, entities, type_override=None, source=None):
        """ helper to create an EntityCollection from given entities

        Args:
            entities (Entity or list): Entity subclass or list of Entity subclasses
            source (EntityCollection or tuple(str, EntityCollection)): store what source produced the new collection
            to preserve the source, from where the resulting EmptyCollection was generated from.
            type_override: if given it will use the override as the type for the generated collection
                and not determine it from the first entity automatically

        Returns:
            EntityCollection
        """
        if not entities:
            if type_override:
                type_override = type_override()
            return EmptyCollection(session=self._session, _type=type_override or self._entity, source=source)

        if isinstance(entities, Entity):
            # TEST: list() constructor too slow, why???
            entities = [entities]

        _entities = OrderedDict(
            [
                (_.id,  _ if not type_override else Entity.from_entity_type(type_override.__name__, _.ftrack_entity))
                for _ in entities
            ]
        )

        # This is just a temporary "solution".
        # We hit the situation that our first entity type lookup results in being a `FileComponent`, whereas
        # other entities can be of type `Component`, which is an unlucky case that lead to fundamental problem
        # when fetching. We need to ensure we don't give subclasses the precedence here!
        # This sorting acts as a very cheap way and we assume that a subclass of a specific type will always
        # include its base type in the name.
        _entity_types = sorted(
            list(set([_.__class__ for _ in _entities.values()])),
            key=lambda x: len(x.__name__.split(".")[-1])
        )

        # TODO: handle ForwardDeclaration

        entities = EntityCollection(
            _cls=type_override or _entity_types[0],
            entities=_entities,
            session=self._session
        )

        entities.query = self.query
        entities.query.valid = False
        entities._source = source

        return entities

    def group(self, predicate):
        """ Returns a dictionary with keys given by the predicate. All entities
        from the original collection will be mapped to their corresponding key.

        Examples:
            >>> groups = asset_versions.group(lambda x: x.asset.name)
            >>> print(groups)

            {
                "gurke_aa": EntityCollection[AssetVersion],
                "banane_ab": EntityCollection[AssetVersion]
            }

        Args:
            predicate (callable): callable object that returns an attribute value

        Returns:
            dict: dictionary including the given predicate result as key and an
            EntityCollection as value
        """
        temp = defaultdict(list)
        groups = {}

        for entity in self:
            temp[predicate(entity)].append(list(entity.values())[0])

        for group, entities in temp.items():
            groups[group] = self.from_entities(entities)

        return groups

    def fold(self, startvalue, predicate):
        """ Accumulates the value starting with an initial value and applying
        an operation from the first to the last element in a collection.

        Args:
            startvalue (Any): it can be anything!!!!
            predicate (callable): callable object that returns an attribute value

        Returns:
            Type(startvalue): Value based on the folding.

        """
        for entitycollection in self:
            startvalue = predicate(startvalue, entitycollection)
        return startvalue

    def map(self, predicate):
        """ Returns a list of results that is obtained by running the predicate
        with each Entity as it's argument and returning the result.
        """
        return map(predicate, self)

    def group_and_map(self, group_predicate, map_predicate):
        """ Runs a group_by first and then runs map on all the Collection in
        the resulting dictionary values.
        """
        groups = self.group(group_predicate)

        mapped_groups = {}
        for key, value in groups.items():
            mapped_groups[key] = map_predicate(value)

        return mapped_groups

    def count(self, predicate):
        """ Returns the number of elements for which the predicate returns True

        Args:
            predicate (callable): callable object that returns an attribute value

        Returns:

        """
        return len(self.filter(predicate))

    def max(self, predicate):
        """ Returns the first element yielding the largest value of the given function.

        Args:
            predicate (callable): callable object that returns an attribute value

        Returns:
            EntityCollection: A new EntityCollection containing the maximum Element

        """
        return self.sort(predicate)[-1]

    def min(self, predicate):
        """ Returns the first element yielding the smallest value of the given function.

        Args:
            predicate (callable): callable object that returns an attribute value

        Returns:
            EntityCollection: A new EntityCollection containing the minimum Element

        """
        # If multiple entities have the same min value, we follow python's min implementation
        # by returning the first occurence of this value. In contrast, the max implementation
        # returns the last occurence.
        _sorted = self.sort(predicate)
        min_value = predicate(_sorted[0])
        return _sorted.filter(lambda x: predicate(x) == min_value)[0]

    def sort(self, predicate, reverse=False):
        """ Returns a duplicate of the original collection sorted by the given predicate.

        Args:
            predicate (callable): callable that returns a comparable object / value
            reverse (bool): reverse the sorting order

        Returns:
            EntityCollection: A duplicate of the original collection sorted by the given predicate.

        """

        entity_collections = sorted(self, key=lambda x: max(predicate(x)), reverse=reverse)

        if len(entity_collections) > 1:
            return entity_collections[0].union(*entity_collections[1:])
        else:
            return entity_collections[0]

    def filter(self, predicate):
        """ Filters the EntityCollection based on a given predicate.

        The predicate is run on each Entity and returns a boolean (or is coerced
        to a boolean). If True, the Entity will be added to the resulting
        collection, if False it will not be added.

        Args:
            predicate (callable): most likely a lambda referring to an entity attribute

        Returns:
            EntityCollection: filtered collection

        """

        filtered = []

        for entitycollection in self:
            if predicate(entitycollection):
                for entity in entitycollection.values():
                    filtered.append(entity)

        if filtered:
            return self.from_entities(filtered)
        else:
            return EmptyCollection(_type=self._entity, source=self._get_parent(self), session=self._session)

    def apply(self, predicate, attribute_name=None):
        """Applies a predicate function to each entity in the collection and
        assigns the generated value to the specified attribute.
        If no attribute name is provided, the value is directly assigned to the calling collection.

        Examples:
            >>> some_collection.apply(lambda c: c.another_attr[0] + "_edited", "some_attr")
            >>> assetversion_collection.Task.Status.apply(status_collection)

        Args:
            predicate (callable): A callable function that receives a single entity collection.
                The return value of the function will be applied to the specified attribute.
            attribute_name (optional: str): The name of the attribute to which the generated value will be assigned
                or None

        Returns:
            EntityCollection: the updated collection

        """
        if not attribute_name:
            attribute_name, collection = self._source
        else:
            collection = self

        for entitycollection in collection:
            setattr(entitycollection, attribute_name, predicate(entitycollection))

        return getattr(collection, attribute_name)

    @staticmethod
    def _get_parent(entitycollection):
        parent_relation = entitycollection._entity.relationship.parent or "parent"
        parents = getattr(entitycollection, parent_relation)
        if not isinstance(parents, (EntityCollection, EmptyCollection)):
            entitycollection.fetch_attributes(parent_relation)
            parents = getattr(entitycollection, parent_relation)

        msg = "Cannot determine singular parent. `{}` ".format(entitycollection)
        if not parents:
            LOG.warning(msg + "has no parents.")
        elif len(parents) > 1:
            LOG.warning(msg + "has multiple parents.")

        return parents

    def partition(self, predicate):
        """ Splits original collection into tuple of EntityCollections,
        where the first EntityCollection contains elements for which the predicate returned True,
        while the second EntityCollection contains elements for which the predicate returned False.

        Args:
            predicate (callable):

        Returns:
            tuple: A tuple including the positive results first and negative results second

        """
        positive, negative = [], []

        for entitycollection in self:
            if predicate(entitycollection):
                for entity in entitycollection.values():
                    positive.append(entity)
            else:
                for entity in entitycollection.values():
                    negative.append(entity)

        return self.from_entities(positive), self.from_entities(negative)

    def union(self, *collections):
        """ Returns an EntityCollection with elements belonging to the current or the given collection or possibly both

        Args:
            collections (EntityCollection): EntityCollection object of same type as the current one

        Returns:
            EntityCollection:

        """
        entities = list(self.values())
        for collection in collections:
            if not collection:
                continue  # avoid merging EmptyCollections
            self._validate_collection_type(collection)
            for entity in collection:
                if list(entity.values())[0] not in entities:
                    entities.append(list(entity.values())[0])

        return self.from_entities(entities)

    def intersection(self, *collections):
        """ Returns an EntityCollection with elements belonging to the current and the given collection

        Args:
            collections (EntityCollection): EntityCollection object of same type as the current one

        Returns:
            EntityCollection:

        """
        for collection in collections:
            self._validate_collection_type(collection)

        intersection = []
        for _id in self.keys():
            if all(_id in collection.keys() for collection in collections):
                intersection.append(_id)

        return self.filter(lambda x: x.id[0] in intersection)

    # TODO: Mathematically this is a binary operation and needs to be applied in a specific order.
    #  The current implementation could be renamed to 'unique' or similar.
    # FIX: The current implementation of symmetric difference does not return
    #  the expected result.
    def symmetric_difference(self, *collections):
        """ Returns an EntityCollection with elements belonging possibly to the
        current and the given collection, but never to both.

        Args:
            *collections (EntityCollection): EntityCollection objects of same
             type as the current one

        Returns:
            EntityCollection
        """
        for collection in collections:
            self._validate_collection_type(collection)

        counter = defaultdict(int)

        all_collections = [self] + list(collections)
        all_entities = self.union(*collections)

        for collection in all_collections:
            for entity in collection.values():
                counter[entity] += 1

        difference = [entity for entity in all_entities.values() if counter[entity] == 1]

        return self.from_entities(difference)

    def difference(self, *collections):
        """ Generates the difference between self and the given collections.

        This essentially acts as a "subtraction" operation.

        Returns:
            EntityCollection
        """

        ids = self.keys()

        for collection in collections:
            ids = [_id for _id in ids if _id not in collection.keys()]

        return self.filter(lambda x: x.id[0] in ids)

    def _validate_collection_type(self, collection):
        """ Compares a given collection type with the collection type of self.

        Raises an error if the collections are not compatible i.e. we can't
        store their entities in the same collection.
        """

        # TODO: allow set operations if the source collection is a parent type of the given collection type
        #  This is useful if you have a EntityCollection[TypeContext] you want to operate on
        # is_valid = True
        # parent_types = ["TypedContext", "List"]
        #
        # if self.entity_type != collection.entity_type:
        #     is_valid = False
        #     if (self.values() and collection.values()) and list(self.values())[0].__class__.__name__ in parent_types:
        #         if issubclass(list(collection.values())[0].__class__, list(self.values())[0].__class__):
        #             is_valid = True
        #
        # if not is_valid:
        #    ...

        if self.entity_type != collection.entity_type:
            raise EntityCollectionOperationError(
                "Only EntityCollections of same type can be used for Set operations. "
                "Expected {}, got {}".format(repr(self), repr(collection))
            )

    def as_query(self, use_ids=False, with_projections=False):
        # TODO(high): To support dynamic ftrack entities we need to have the
        #  possibility to use different attributes than id in this case.
        #  Potentially use ftrack_api.session.populate for fetching!.
        # TEST: How do we know that we have a dynamicftrackentity:
        #  Generalize handling of non fixed primary keys.
        if use_ids or not self.query.valid:
            self.query.criteria = [
                Criterion(
                    name="by_id",
                    args=tuple(self.keys()),
                    kwargs={},
                    target=None,
                    filter=self._entity.by_id
                )
            ]
            if not with_projections:
                self.query.projections = []
            self.query.entity_type = self._entity

        return self.query

    def fetch_attributes(self, *attributes):
        """ Fetches the given attributes from ftrack by doing another query.
        This allows access if auto population is disabled

        Args:
            *attributes (str): attributes (can be scoped)
        """

        def _deepen(iterables):
            nested = {}
            for iterable in iterables:
                temp = nested
                for value in iterable:
                    if not temp.get(value):
                        temp[value] = {}
                    temp = temp[value]
            return nested

        def _flatten(iterable):
            def __flatten(iterable, path=""):
                flat = {}
                if len(iterable.keys()) == 1:
                    # we are on a non branching level
                    key = list(iterable.keys())[0]
                    # append to the existing path as we don't need to branch
                    path += "." + key if path else key  # only insert dot in existing path
                    # get the downstream dict recursively
                    if key.endswith("]"):
                        _ = __flatten(iterable[key], "")
                    else:
                        _ = __flatten(iterable[key], path)
                    # if the downstream level will not branch either, we move the dict
                    # up one level. this is also done if we split due to a type
                    # specialization e.g. [Shot]
                    if len(_.keys()) == 1 and not key.endswith("]"):
                        return _
                    # otherwise we insert a level for a branch
                    flat[path] = _
                    return flat
                elif len(iterable.keys()) > 1:
                    # we are on a branching level
                    for key, value in iterable.items():
                        if len(value.keys()) == 1:
                            # if the child will not branch, we will reset the
                            # hierarchy to not accumulate duplicate levels
                            path = ""
                        _ = __flatten(value, path)
                        if len(_.keys()) == 1:
                            # if the childs are not branching we extract the values
                            # and set them with the correct key
                            flat[key + "." + list(_.keys())[0]] = list(_.values())[0]
                        else:
                            # otherwise we will create a new branch
                            flat[key] = _
                    return flat
                return flat

            flat = __flatten(iterable)
            return flat

        def _get_attribute(entity, attributes):
            attribute_tokens = attributes.split(".")

            parent = entity
            for token in attribute_tokens:
                if token.endswith("]"):
                    token, _type = token.split("[")
                entity = getattr(parent, token)
                # TODO: this is not ideal, we shouldn't run into this situation
                #  so we probably have to improve the _flatten function
                if isinstance(entity, list) and NOT_SET in entity:
                    _fetch(parent, {token: {}})
                    entity = getattr(parent, token)

                parent = entity

            return entity

        def _fetch(entities, attributes):
            # TODO(nice to have): Can we potentially do a fetch on an EmptyCollection by using the 'source' attribute?
            #  This is only possible if we fetch into the direction of the source attribute.
            if isinstance(entities, EmptyCollection):
                LOG.info("Encountered an `EmptyCollection` while fetching attributes. Can't continue fetching.")
            else:
                query = entities.as_query(use_ids=True)
                if isinstance(attributes, dict):
                    _bases = query.entity_type.__class__.__bases__

                    # There is the chance of getting a collection containing different types
                    # of the same base type when constructed via _get_attribute(), as we don't handle filtering
                    # like parent[AssetBuild]. This leads to the situation that our query would only fetch the
                    # requested attributes for type of the first entity in the collection. Therefore we have to
                    # ensure we use the base type when fetching.
                    if _bases and _bases[0].__name__ in ["TypedContext"]:
                        query.entity_type = _bases[0]()

                    query.projections = [_.split("[")[0] for _ in attributes.keys()]
                    query.get_all()

                    for key, value in attributes.items():
                        entity = _get_attribute(entities, key)
                        if not isinstance(entity, list):
                            _fetch(entity, value)
                else:
                    query.projections = attributes
                    query.get_all(session=self._session)

        # lets resolve all RelationshipDeclarations first
        _attributes = []
        for attribute in attributes:
            if isinstance(attribute, RelationshipDeclaration):
                _attributes.extend(attribute.resolve_path_for(self.entity_type, self.query.session, self.query.schema))
            else:
                _attributes.append(attribute)

        attributes = [attribute.split(".") for attribute in _attributes]
        deep = _deepen(attributes)
        flat = _flatten(deep)
        # attribute_hierarchy = _flatten(_deepen(attributes))
        _fetch(self, flat)

        return self

    def _simple_children_fetch(self, *attributes):
        # this is needed as a special case to avoid an infinite recursion due to
        # fetch_attributes calling getattr and getatrr calling fetch_attributes
        # (wheh accessing children)
        query = self.as_query(use_ids=True)
        # TODO(high): Reimplement the conditional fetching of non-existing projections.
        # Update the projections on the query object accordingly.
        # only perform a query if really necessary
        if set(attributes).union(query.projections) != set(query.projections):
            query.projections = list(set(attributes).union(query.projections))  # update not override
            query.get_all()
        else:
            LOG.info("All requested attributes already set.")

    def commit(self):
        self._session.commit()

    def _get_relatives(self, relative_type, **kwargs):
        """ Get the relative entity based on the relationship.

        Args:
            relative_type (Entity): subclass of Entity
            **kwargs ():

        Returns:
            Any: whatever the attributes holds, most likely another EntityCollection
        """

        relationship = self.query.entity_type.relationship.get(relative_type, default=TargetRelation()).relation
        if not relationship:
            raise ValueError("Unknown relationship for relative '{}'".format(relative_type))

        if not isinstance(relationship, list):
            relation_projections = [relationship]
        else:
            relation_projections = relationship

        outside_projections = kwargs.get("projections", [])
        constructed_projections = []

        for outside_projection in outside_projections:
            for relation_projection in relation_projections:
                constructed_projections.append("{}.{}".format(relation_projection, outside_projection))

        if not outside_projections:
            constructed_projections.extend(relation_projections)

        self.fetch_attributes(*constructed_projections)

        return getattr(self, relative_type.__name__)

    def _prepare_note_entity(self, ftrack_note_entity, kwargs, parent_source):
        """ preparation of a node entity

        This shall ensure we don't have to pass author and recipients for `notes.create()`.

        Args:
            ftrack_note_entity (entity): the ftrack api entity instance

        Returns:

        """
        # TODO: this definitely needs cleanup
        # make the Query class available
        _Query = getattr(importlib.import_module("...query", __name__), "Query")

        # get the actual entity implemantions not the ForwardDeclare classes
        _Recipient = getattr(importlib.import_module("..entities", __name__), "Recipient")
        _User = getattr(importlib.import_module("..entities", __name__), "User")

        if not ftrack_note_entity.get("author"):
            ftrack_note_entity["author"] = list(_Query(_User, session=self._session).by_name(
                self._session.api_user).get_one().values())[0].ftrack_entity

        recipients = ftrack_note_entity.get("recipients", [])
        if not recipients:
            resource_ids = kwargs.get("recipient_resource_ids", [])
            recipients = _Query(_Recipient, session=self._session).get_first()
            if not resource_ids:
                resource_ids = [ftrack_note_entity["author"]["id"]]

            for resource_id in resource_ids:
                recipient = recipients.create(
                    note_id=ftrack_note_entity["id"],
                    resource_id=resource_id
                )
                ftrack_note_entity["recipients"].append(list(recipient.values())[0].ftrack_entity)

        # The parent source is a sibling collection, reuse it's parent attrs
        if parent_source.entity_type.__name__ == "Note":
            parent_source.fetch_attributes("parent_type", "parent_id")
            # TODO: improve error message when context is ambiguous
            assert len(set(parent_source.parent_id)) == 1, "Ambiguous context. Multiple parents found."
            ftrack_note_entity["parent_id"] = parent_source.parent_id[0]
            ftrack_note_entity["parent_type"] = parent_source.parent_type[0]

        # The parent source is a the actual parent of the node, use it's attributes to
        # create the first note.
        else:
            ftrack_note_entity["parent_id"] = parent_source.id[0]
            ftrack_note_entity["parent_type"] = parent_source._entity.__class__.__name__

    def create(self, **kwargs):
        """
        Creates a new Entity based on the current context.

        The context is defined by self as well as the potential parent attribute.
        If a parent is set in the relationships of an Entity, we will use that,
        otherwise we simply assume an attribute name of "parent".
        We can also ignore the requirement of a parent by providing the
        no_parent keyword argument (the value does not matter). This is useful
        for entities that don't require (or have) a parent, like Project.

        Args:
            **kwargs: A dictionary of data that is required to initialize the
            Entity properly.

        Returns:
            An EntityCollection with the created Entity.

        """

        # TODO: Handle creation of dynamic ftrack entities.
        # TODO: this can fail if we have not specified a parent relation and
        #  the default relation does not exist. In this case we would fetch a
        #  non existing attribute which will fail. Raise a clear assertion which
        #  describes the exact circumstances of the failure.
        #  At the same time it is required to have the 'no_parent' set.

        # checking for the "empty" kwarg enables us to create new Entities
        # without requiring preexisting siblings.
        if "empty" in kwargs:
            this = kwargs.get("empty")
            parent = this.source
            parent_relation = kwargs.get("parent_relation", None) or this._entity.relationship.parent or "parent"
            del kwargs["empty"]
        else:
            this = self
            parent_relation = kwargs.get("parent_relation", None) or this._entity.relationship.parent or "parent"

            if parent_relation in list(this.values())[0].ftrack_entity.keys():
                if not all(getattr(this, parent_relation)):
                    this.fetch_attributes(parent_relation)

                parent = getattr(this, parent_relation)
            else:
                kwargs["no_parent"] = True

        # pre-process the keyword arguments for the corresponding entity type
        kwargs["session"] = self._session
        kwargs = this._entity.pre_create(**kwargs)

        if "no_parent" not in kwargs.keys():
            # TODO: improve error message when context is ambiguous
            assert len(parent) == 1, "Ambiguous context. Multiple parents found."

            kwargs.update(
                {parent_relation: list(parent.values())[0].ftrack_entity}
            )

        assert isinstance(kwargs, dict), "pre_create method returned something that is not a dict"

        entity_class_name = this._entity.__class__.__name__
        ftrack_entity = self._session.create(entity_class_name, data=kwargs)

        # specific handling for anything that can't be easily achieved within the pre-create method
        if entity_class_name == "Note":
            # When the entity we have doesn't have any notes, we can use "parent" as the
            # source of information, this will be the collection from which the notes are
            # being created.
            if isinstance(parent, EntityCollection):
                note_parent_source = parent
            # If the collection already has some notes, "this" will be the collection
            # for the existing siblings, we can then use those to extract the information.
            else:
                note_parent_source = this
            self._prepare_note_entity(ftrack_entity, kwargs, parent_source=note_parent_source)

        entity = this._entity.__class__(_cls=this._entity.__class__, ftrack_entity=ftrack_entity)

        return self.from_entities([entity])

    def create_batch(self, *attributes):
        """ Calls "create" in a loop to create multiple entities and store all
        of them in an EntityCollection.


        Args:
            *attributes (dict): Multiple dictionaries with key-value-pairs that
            will be used as the keyword arguments for the "create" call.

        Returns:
            An EntityCollection with all the Entities that have been created.
        """

        collections = []

        for _attributes in attributes:
            collections.append(self.create(**_attributes))

        return EmptyCollection(_type=self._entity, session=self._session).union(*collections)

    def delete(self):
        """ Deletes all Entities in self from ftrack.

        Returns:
            The SESSION object so we can call commit() directly.
        """
        type_name = self.entity_type.__name__
        if not ALLOWED_FOR_DELETION_RESOLVER(session=self._session, type_name=type_name):
            raise AssertionError(
                "Current entity type '{}' for server '{}' is not allowed for deletion. ".format(
                    type_name,
                    self._session.server_url
                )
            )

        for entity in self.values():
            ftrack_entity = entity.ftrack_entity
            LOG.info("Deleting Entity '{}'".format(ftrack_entity))
            self._session.delete(ftrack_entity)

        return self._session


class _EntityBase(object, metaclass=ForwardDeclareCompare):

    relationship = Relationship()
    projections = ["id"]
    _ftrack_entity = None
    log = None

    def __new__(cls, *args, **kwargs):
        """ make it possible to swap the Entity class with the given class

        Args:
            *args ():
            **kwargs ():

        Returns:

        """
        if kwargs.get("_cls"):
            cls = kwargs["_cls"]
            cls.log = logging.getLogger("{}.entities.{}".format(cls.__name__, LOGGING_NAMESPACE))
            del kwargs["_cls"]

        if cls and args and isinstance(args[0], (EntityCollection, EmptyCollection)):
            source_collection = args[0]

            if source_collection:
                _cls = source_collection.entity_type
            else:
                _cls = source_collection.entity_type.__class__

            assert issubclass(_cls, cls), \
                "Can't coerce `{source}` to `{target}`, because `{source}` is not a subtype of `{target}`.".format(
                    source=_cls.__name__,
                    target=cls.__name__,
                )

            _source = getattr(source_collection, "source", None)

            target_collection = source_collection.from_entities(
                source_collection.values() or [],
                type_override=cls,
                source=_source
            ) or \
            EmptyCollection(
                session=source_collection._session,
                _type=cls(),
                source=_source
            )  # TODO:  shall we implement from_entities on EmptyCollection?

            return target_collection

        return super(_EntityBase, cls).__new__(cls)

    def __init__(self, _cls=None, ftrack_entity=None, **kwargs):
        self.ftrack_entity = ftrack_entity
        if not _cls:
            self.log = logging.getLogger(
                "{}.entities.{}".format(self.__class__.__name__, LOGGING_NAMESPACE)
            )

    def __getitem__(self, item):
        return self.ftrack_entity.get(item)

    def __getattr__(self, item):
        value = None
        if item in self.ftrack_entity.keys():
            value = self.ftrack_entity[item]
            if hasattr(value, "entity_type"):
                return Entity.from_entity_type(str(value.entity_type), ftrack_entity=value)
        return value

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash(self.ftrack_entity["id"])

    def __eq__(self, other):
        # TEST: Figure out how to avoid this behaviour and ditch this workaround.
        #  weirdly there is a possibility that this is executed with classes as
        #  self (which by definition should NEVER be class) and other
        #  (for example when comparing EmptyCollections)
        #  see TestRelativeTerminators for an example
        #  Additionally, this should actually work, as we've overridden __eq__
        #  in the metaclass which should take care of class comparisons
        if inspect.isclass(self) and inspect.isclass(other):
            return self == other
        elif isinstance(self, Entity) and isinstance(other, Entity):
            return self.ftrack_entity == other.ftrack_entity
        else:
            return False

    def __cmp__(self, other):
        if self == other:
            return 0
        else:
            return 1

    def pre_create(self, **kwargs):
        return kwargs

    @property
    def ftrack_entity(self):
        return self._ftrack_entity

    @ftrack_entity.setter
    def ftrack_entity(self, instance):
        self._ftrack_entity = instance

    @classmethod
    def from_entity_type(cls, name, ftrack_entity=None):
        entity_cls = getattr(importlib.import_module("..entities", __name__), str(name))
        if not issubclass(entity_cls, Entity):
            raise NotImplementedError("The Entity of type \"{}\" has not been implemented yet.".format(entity_cls.__name__))
        return cls(_cls=entity_cls, ftrack_entity=ftrack_entity)

    # These methods are only here so the stubs builder can automatically add them.
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None): pass
    def get_first(self, projections=None): pass
    def get_one(self, projections=None): pass
    def get_all(self, projections=None): pass
    def get_inputs(self, projections=None): pass
    def get_outputs(self, projections=None): pass

    def create(self, **kwargs): pass
    def create_batch(self, *attributes): pass
    def delete(self): pass

    # although there is no logical reason to have multiple filters
    # this is how the query consolidates its criteria
    # having multiple filters allows us the inject criterion multiple times
    # Example:
    #   Query(Task).inject("parent.parent.name is 'library').by_name(Project, "Foobar").inject("parent.status.name is 'Approved').get_all()
    def inject(self, target, *filter):
        if any(re.search(r"^or\s*", _, flags=re.IGNORECASE) for _ in filter):
            raise ValueError(
                "OR relationships are not supported across multiple criteria or filter.\n"
                "You can use an 'or' relationship within a single filter string though."
            )

        # sanitize partial query
        sanitized_filters = [re.sub(r"^(and|where)\s*", "", _, flags=re.IGNORECASE) for _ in filter]
        partial_query = " and ".join(sanitized_filters)
        if WARN_ON_INJECT:
            self.log.warning("`inject` criteria was used with partial query '{}'".format(partial_query))

        return partial_query


class Entity(_EntityBase):

    @Criteria.supported_targets(_EntityBase)
    def by_id(self, target, *ids):
        target = target or TargetRelation()
        return utils.build_partial_query(target, ids, "id")

    @Criteria.supported_targets(_EntityBase)
    def by_metadata(self, target, *dictionaries):
        query = "("
        for _dict in dictionaries:
            query += "("
            for key, value in _dict.items():
                if target:
                    query += "{}.".format(target.relation)
                query += "metadata any (key like \"{}\" and value like \"{}\") and ".format(key, value)
            query = query[:-5] + ") or "
        query = query[:-4] + ")"
        return query


class EntityCollectionOperationError(ValueError):
    pass


