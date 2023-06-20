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
import logging
import re

from collections import OrderedDict
from copy import (
    copy,
    deepcopy
)
import wrapt

import ftrack_api


from .criteria import (
    Criterion,
    Criteria
)
from ..entities.base import (
    Entity,
    EntityCollection,
    EmptyCollection
)
from ..entities.declarations import (
    ForwardDeclareCompare,
    RelationshipDeclaration
)
from ..session import SESSION

from ..configuration import (
    RELATIONSHIPS_RESOLVER,
    LOGGING_NAMESPACE
)
from ..constants import __VERSION__


LOG = logging.getLogger("{}.query".format(LOGGING_NAMESPACE))


class QuerySchema(object):

    def __init__(self, relationships, default_schema="default"):

        primary_keys_to_exclude = ["overrides"]
        primary_entities = relationships.get("entities", {})
        setattr(self, default_schema, {})
        getattr(self, default_schema)["name"] = default_schema
        for key, value in relationships.items():
            if key not in primary_keys_to_exclude:
                getattr(self, default_schema).update({key: value})

        for override in relationships.get("overrides", []):
            overrides = {"entities": {}, "name": override["name"]}
            entities = deepcopy(primary_entities) if override.get("inherit", True) else {}
            if entities:
                overrides["entities"] = entities

            for key, value in override["entities"].items():
                per_entity_relationships = overrides["entities"].get(key, {})
                per_entity_relationships.update(value)
                overrides["entities"][key] = per_entity_relationships

            setattr(self, override["name"], overrides)

    def __getitem__(self, item):
        try:
            return getattr(self, item)
        except AttributeError:
            raise KeyError("Schema '{}' doesn't exist".format(item))


SCHEMA = QuerySchema(RELATIONSHIPS_RESOLVER(api_version=__VERSION__))
_NEGATION_CRITERION_PATTERN = r"^not_by_"


class Query(object):
    """ wraps the ftrack query language

    """

    _known_order = ["ascending", "descending"]

    def __init__(self, entity, session=SESSION, schema=SCHEMA.default):
        self.entity_type = entity()

        self.entity_type.relationship(session=session, schema=schema)

        self.primary_key = self.entity_type.projections[0] if len(self.entity_type.projections) else "id"
        self.projections = []
        self.criteria = []
        self.session = session
        self.schema = schema
        self._valid = False

    def __getattribute__(self, item):
        """ forwarding of criteria methods to the specific entity implementation """

        is_negation = bool(re.match(_NEGATION_CRITERION_PATTERN, item))
        has_criterion = hasattr(Criteria, item)
        if is_negation:
            criterion_counterpart = re.sub(_NEGATION_CRITERION_PATTERN, "by_", item)
            if hasattr(Criteria, criterion_counterpart):
                item = criterion_counterpart
                has_criterion = True

        # check if item is a known criterion
        if has_criterion and item not in dir(type):
            # check if criterion was implemented on entity
            if not hasattr(self.entity_type, item):
                raise Criteria.CriterionNotImplementedError(
                    "Criterion `{}` is not implemented on entity {}.".format(item, self.entity_type)
                )

            return self._magic(getattr(self.entity_type, item), negate=is_negation)

        return super(Query, self).__getattribute__(item)

    def __copy__(self):
        query = Query(self.entity_type.__class__, session=self.session, schema=self.schema)
        query.projections = copy(self.projections)
        query.criteria = copy(self.criteria)
        query.valid = self.valid
        return query

    def __str__(self):
        """ returns the generated query string """

        projections = ", ".join(self.projections or self.entity_type.projections)

        _query = "select {} from {}".format(
                projections,
                self.entity_type.__class__.__name__
            )

        if self.criteria:
            # We sort the criteria based on the distance to the queried entity:
            # distance(parent) = 0
            # distance(parent.parent.name) = 2
            # This will make the query much more efficient.
            _query += " where {}".format(
                    " and ".join(sorted(
                        [_.resolve() for _ in self.criteria],
                        key=lambda x: len(x.split(".")))
                    )
            )

        return _query

    def _get_shared_criterion(self, criterion):
        """ detect if criterion already exists

        Args:
            criterion (Criterion): Criterion object

        Returns:
            bool: True if it can be considered as shared
        """
        _existing = [_ for _ in self.criteria if _.name == criterion.name and _.negate == criterion.negate]
        if _existing:
            if _existing[0] and _existing[0].target == criterion.target:
                return _existing[0]

    def _store_criterion(self, criterion):
        """ detect and merge with same existing criterion

        Args:
            criterion (Criterion): Criterion object

        Returns:

        """
        existing = self._get_shared_criterion(criterion)
        if not existing:
            self.criteria.append(criterion)
        elif existing.args != criterion.args:
            _data = existing.as_dict()
            # append new arguments
            _data["args"] += criterion.args

            index = self.criteria.index(existing)
            self.criteria.remove(existing)
            self.criteria.insert(index, Criterion(**_data))

    def _extract_target(self, args):
        if not args:
            return None, args
        target_cls = args[0]
        if not inspect.isclass(target_cls):
            target_cls = None
            arguments = args
        else:
            arguments = args[1:]
        return target_cls, arguments

    @staticmethod
    def _validate_criteria_signature(func, target, args, kwargs):
        caller_name = func.__name__
        if target and (bool(args) is bool(kwargs)):
            raise Criteria.InvalidArgumentsError(
                "You provided a target, but either NO arguments and NO keyword arguments "
                "or arguments AND keyword arguments in `.{}()`. Both possibilities are "
                "not supported.".format(caller_name)
            )
        elif not target and not args and not kwargs:
            raise Criteria.InvalidArgumentsError(
                "You gave us nothing. NOTHING!!!! `.{}()` is very sad.".format(caller_name)
            )

    def _construct_entity_collection(self, result):
        _cls = self.entity_type.__class__
        if result:
            if isinstance(result, list):
                entities = OrderedDict((_[self.primary_key], Entity(_cls=_cls, ftrack_entity=_)) for _ in result)
            else:
                entities = OrderedDict([(result[self.primary_key], Entity(_cls=_cls, ftrack_entity=result))])

            entitycollection = EntityCollection(_cls=_cls, entities=entities)
            entitycollection.query = Query(_cls, session=self.session, schema=self.schema)

            # we use slicing to create copies of our lists
            # that's how we roll bitch (Dennis said)
            entitycollection.query.criteria = self.criteria[:]
            entitycollection.query.projections = self.projections[:]
            entitycollection.query.valid = True

            return entitycollection
        else:
            return EmptyCollection(_type=_cls())

    def _magic(self, func, negate=False):
        """ wrapper for our forwarded criteria functions

        This allows to append the result of the forwarded function to the
        criteria list, but also returns the Query object itself, to allow
        autocompletion for arbitrary amounts of criteria calls
        (all by_* methods defined in the Criteria class).
        """
        def inner(*args, **kwargs):
            target = None
            arguments = ()

            if args:
                target, arguments = self._extract_target(args)
                self._validate_criteria_signature(func, target, arguments, kwargs)

            criterion = Criterion(
                name=func.__name__,
                args=arguments,
                kwargs=kwargs,
                target=target,
                filter=func,
                negate=negate
            )

            self._store_criterion(criterion)

            return self

        return inner

    @wrapt.decorator
    def _fill_target(wrapped, instance, args, kwargs):
        """ decorator for those terminators which commonly support a target (Entity class)
        """
        target, args = instance._extract_target(args)
        return wrapped(target or instance.entity_type.__class__, *args, **kwargs)
    
    def _set_projections(self, projections):
        if projections:
            # resolve unknown projections
            _projections = []
            for projection in projections:
                # prepare for resolution of something like projections=[Asset]
                if isinstance(projection, ForwardDeclareCompare):
                    projection = RelationshipDeclaration(parent=projection, child="")
                # resolved already wrapped - like projections=[AssetBuild.name]
                if isinstance(projection, RelationshipDeclaration):
                    projection = projection.resolve_path_for(self.entity_type, self.session, self.schema)
                    _projections.extend(projection)
                else:
                    _projections.append(projection)
            # extend default projections
            self.projections = list(set(_projections + self.entity_type.__class__.projections))

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        assert isinstance(value, bool), "Invalid value {} for attribute valid.".format(value)
        self._valid = value

    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None):
        """ get the result with limit, offset and specific ordering

        Notes:
            Compared to the default FTrack behavior our order will reflect the
            actual sorting in the end.

        Args:
            limit (int): limited amount of resulting entities
            offset (int): offset
            order (str): "descending" or "ascending"
            order_by (str): field to use for ordering

        Returns:
            Entity subclass: the given entity instance

        """
        assert order in self._known_order, "Unknown specified order '{}'. Supported: {}".format(
            order, ", ".join(self._known_order)
        )
        if projections:
            assert isinstance(projections, (list, tuple, set)), (
                "'projections' expect any of the following types: list, tuple, set. Got: {}".format(type(projections))
            )

        self._set_projections(projections)

        query = str(self)

        if limit:
            query += " limit {}".format(limit)
        if offset:
            query += " offset {}".format(offset)
        if order_by:
            query += " order by {} {}".format(order_by, order)
        if limit and not order_by:
            # TODO: if we query a <dynamic ftrack Recipient object 139776416590416>
            #  which does not have an id this will fail. In this case we need to
            #  sort by a different key
            #  We probably have to dynamically get the primary key and use that
            #  for sorting
            # TEST: Is this solved via the primary key?
            query += " order by {}".format(self.primary_key)

        # In case the same query is reused multiple times, we can lookup a
        # previous result and skip the actual query.
        if self.session.reuse_query_results and query in self.session._terminated_queries:
            LOG.debug("Reuse cached query '{}'".format(query))
            return self.session._terminated_queries[query]

        LOG.info("Performing query: \"{}\"".format(query))
        result = self.session.query(query).all()

        if order_by:
            result = sorted(result, key=lambda x: x[order_by], reverse=(order == "descending"))

        # TODO: if result is empty we need to add the entity type information
        #  to the resulting EmptyCollection
        # TEST: Check if this is already solved.
        entities = self._construct_entity_collection(result)
        entities._session = self.session
        if not entities:
            LOG.warning("Query '{}' returned no results.".format(self))

        # TODO: should we only store the result in case it produced a collection?
        # original query
        self.session._terminated_queries[query] = entities
        # query with original projections
        self.session._terminated_queries[str(entities.as_query(use_ids=True, with_projections=True))] = entities
        # query with exclusive default projections
        self.session._terminated_queries[str(entities.as_query(use_ids=True))] = entities

        return entities

    def get_one(self, projections=None):
        result = self.get(projections=projections, limit=2)
        if len(result) > 1:
            raise ftrack_api.exception.MultipleResultsFoundError("Multiple results found for '{}'".format(self))
        if not result:
            raise ftrack_api.exception.NoResultFoundError("No result found for '{}'".format(self))

        return result

    def get_first(self, projections=None, offset=0):
        return self.get(projections=projections, limit=1, offset=offset)

    def get_all(self, projections=None, limit=None, offset=0, order="ascending", order_by=None):
        return self.get(
            projections=projections,
            limit=limit,
            offset=offset,
            order=order,
            order_by=order_by,
        )
    
    @_fill_target
    def get_inputs(self, target, projections=None):
        in_ids = self.get_all(projections=['incoming_links.from_id']).incoming_links.from_id
        if in_ids:
            inputs = Query(target, session=self.session, schema=self.schema) \
                .by_id(*in_ids) \
                .get_all(projections=projections)
            return inputs
        return EmptyCollection(_type=target(), session=self.session)
    
    @_fill_target
    def get_outputs(self, target, projections=None):
        out_ids = self.get_all(projections=['outgoing_links.to_id']).outgoing_links.to_id
        if out_ids:
            outputs = Query(target, session=self.session, schema=self.schema) \
                .by_id(*out_ids) \
                .get_all(projections=projections)
            return outputs
        return EmptyCollection(_type=target(), session=self.session)
