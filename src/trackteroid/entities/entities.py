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

from .base import *
from .declarations import *
from ..query import Criteria
from ..query.utils import build_partial_query
from .schematypes import (
    ASSET_TYPES,
    OBJECT_TYPES,
    TASK_TYPES,
    PROJECT_SCHEMAS
)


class AssetVersion(Entity):
    projections = ["id", "asset.name", "version"]

    relationship = Relationship()
    relationship.parent = "asset"

    def pre_create(self, **kwargs):
        """ pre process before create() call

        Validates and modifies passed keyword arguments from create()

        Args:
            **kwargs (): incoming keyword arguments from create(**kwargs)

        Returns:

        """
        super(AssetVersion, self).pre_create(**kwargs)

        assert "task" in kwargs, "task is a required keyword argument"
        assert len(kwargs["task"]) == 1, "AssetVersions have to be linked to a single task. You provided {}.".format(
            len(kwargs["task"])
        )
        assert isinstance(kwargs["task"], EntityCollection), "Argument 'task' expects a value of EntityCollection[Task]"

        kwargs["task"] = list(kwargs["task"].values())[0].ftrack_entity

        return kwargs

    # only for autocompletion
    def create(self, task, **kwargs): pass
    def link_inputs(self, entity_collection): pass
    def link_outputs(self, entity_collection): pass
    def unlink_inputs(self, entity_collection): pass
    def unlink_outputs(self, entity_collection): pass

    @Criteria.supported_targets(Entity)
    def by_name(self, target, *names):
        target = target or self.relationship[Asset]
        return build_partial_query(target, names, "name")

    @Criteria.supported_targets()
    def by_publisher(self, target, *publishers):
        target = target or TargetRelation()
        return build_partial_query(target, publishers, "user.username")

    @Criteria.supported_targets()
    def by_resource_identifier(self, target, *resource_identifiers):
        target = target or self.relationship[ComponentLocation]
        return build_partial_query(target, resource_identifiers, "resource_identifier")

    @Criteria.supported_targets()
    def by_version(self, target, *versions):
        target = target or TargetRelation()
        return build_partial_query(target, versions, "version")

    @Criteria.supported_targets(Task)
    def by_status(self, target, *statuses):
        target = target or TargetRelation()
        return build_partial_query(target, statuses, "status.name")

    @Criteria.supported_targets(Task)
    def by_state(self, target, *states):
        target = target or TargetRelation()
        return build_partial_query(target, states, "status.state.name")

    @Criteria.supported_targets(Task, Asset)
    def by_type(self, target, *types):
        target = target or self.relationship[Asset]
        return build_partial_query(target, types, "type.name")

    @Criteria.supported_targets()
    def by_publish_time(self, target, start=None, end=None):
        query = "("
        if start:
            query += "date >= \"{}\"".format(start)
        if start and end:
            query += " and "
        if end:
            query += "date <= \"{}\"".format(end)
        query += ")"
        return query

    @Criteria.supported_targets()
    def by_outgoing_link(self, target, *ids):
        target = target or TargetRelation("used_in_versions", collection=True)
        return build_partial_query(target, ids, "id")

    @Criteria.supported_targets()
    def by_incoming_link(self, target, *ids):
        target = target or TargetRelation("uses_versions", collection=True)
        return build_partial_query(target, ids, "id")

    @Criteria.supported_targets()
    def by_publish_state(self, target, publish_state):
        target = target or TargetRelation()
        return build_partial_query(target, [publish_state], "is_published")


class TypedContext(Entity):
    projections = ["id", "name"]
    relationship = Relationship()

    # only for autocompletion
    def link_inputs(self, entity_collection): pass
    def link_outputs(self, entity_collection): pass
    def unlink_inputs(self, entity_collection): pass
    def unlink_outputs(self, entity_collection): pass

    @Criteria.supported_targets(Entity)
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")

    @Criteria.supported_targets(AssetVersion, TypedContext)
    def by_status(self, target, *statuses):
        target = target or TargetRelation()
        return build_partial_query(target, statuses, "status.name")

    @Criteria.supported_targets(AssetVersion, TypedContext)
    def by_state(self, target, *states):
        target = target or TargetRelation()
        return build_partial_query(target, states, "status.state.name")

    @Criteria.supported_targets(Asset, TypedContext)
    def by_type(self, target, *types):
        target = target or TargetRelation()
        return build_partial_query(target, types, "type.name")

    @Criteria.supported_targets()
    def by_status_change_time(self, target, start=None, end=None):
        query = "status_changes any ("
        if target:
            query = "{}.{}".format(target.relation, query)
        if start:
            query += "date >= \"{}\"".format(start)
        if start and end:
            query += " and "
        if end:
            query += "date <= \"{}\"".format(end)
        query += ")"
        return query

    @Criteria.supported_targets()
    def by_assignee(self, target, *assignees):
        target = target or TargetRelation()
        return build_partial_query(target, assignees, "assignments.resource.username")

    @Criteria.supported_targets()
    def by_outgoing_link(self, target, *ids):
        target = target or TargetRelation("outgoing_links", collection=True)
        return build_partial_query(target, ids, "to_id")

    @Criteria.supported_targets()
    def by_incoming_link(self, target, *ids):
        target = target or TargetRelation("incoming_links", collection=True)
        return build_partial_query(target, ids, "from_id")

    @Criteria.supported_targets(Project)
    def by_lifespan(self, target, start=None, end=None):
        query = ""
        if target:
            implicit_target = "{}.".format(target.relation)
        else:
            implicit_target = ""

        if start:
            query += "{}start_date >= \"{}\"".format(implicit_target, start)
        if start and end:
            query += " and "
        if end:
            query += "{}end_date <= \"{}\"".format(implicit_target, end)

        return query


class Task(TypedContext):
    relationship = Relationship()

    def pre_create(self, **kwargs):
        """ pre process before create() call

        Validates and modifies passed keyword arguments from create()

        Args:
            **kwargs (): incoming keyword arguments from create(**kwargs)

        Returns:

        """
        super(Task, self).pre_create(**kwargs)

        session = kwargs["session"]
        assert "name" in kwargs, "name is a required keyword argument"
        assert "type" in kwargs, "type is a required argument"

        assert kwargs["type"] in TASK_TYPES.get("types", session), \
            "Unknown task_type '{}'. Known types: {}".format(kwargs["type"], ", ".join(TASK_TYPES.get("types", session).keys()))
        kwargs["type"] = TASK_TYPES.get(kwargs["type"], session)

        return kwargs

    # only for autocompletion
    def create(self, name, task_type): pass


class Shot(TypedContext):
    relationship = Relationship()

    def pre_create(self, **kwargs):
        """ pre process before create() call

        Validates and modifies passed keyword arguments from create()

        Args:
            **kwargs (): incoming keyword arguments from create(**kwargs)

        Returns:

        """
        super(Shot, self).pre_create(**kwargs)

        assert "name" in kwargs, "name is a required keyword argument"
        return kwargs

    # only for autocompletion
    def create(self, name, **kwargs): pass


class Sequence(TypedContext):
    relationship = Relationship()

    def pre_create(self, **kwargs):
        """ pre process before create() call

        Validates and modifies passed keyword arguments from create()

        Args:
            **kwargs (): incoming keyword arguments from create(**kwargs)

        Returns:

        """
        super(Sequence, self).pre_create(**kwargs)

        assert "name" in kwargs, "name is a required keyword argument"
        return kwargs

    def create(self, name, **kwargs): pass


class AssetBuild(TypedContext):
    relationship = Relationship()


class AssetGroup(TypedContext):
    relationship = Relationship()


class Component(Entity):
    projections = ["id", "name"]

    relationship = Relationship()
    relationship.parent = "version"
    
    @Criteria.supported_targets(Entity)
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")

    @Criteria.supported_targets()
    def by_resource_identifier(self, target, *resource_identifiers):
        target = target or self.relationship[ComponentLocation]
        return build_partial_query(target, resource_identifiers, "resource_identifier")

    @Criteria.supported_targets()
    def by_location(self, target, *component_locations):
        target = target or self.relationship[ComponentLocation]
        return build_partial_query(target, component_locations, "location.name")

    @Criteria.supported_targets()
    def by_file_type(self, target, *file_types):
        target = target or TargetRelation()
        return build_partial_query(target, file_types, "file_type")

    @Criteria.supported_targets(AssetVersion)
    def by_version(self, target, *versions):
        target = target or self.relationship[AssetVersion]
        return build_partial_query(target, versions, "version")

    @Criteria.supported_targets()
    def by_system_type(self, target, *system_types):
        target = target or TargetRelation()
        return build_partial_query(target, system_types, "system_type")

    @Criteria.supported_targets()
    def by_size(self, target, minimum=0, maximum=0):
        """Builds a query expression for filtering by size in bytes.

        Args:
            target (NoneType): unused, but required in signature due to decorator.
            minimum (int): minimum size.
            maximum (int): maximum size.

        Returns:
            str: by size partial query.

        """
        query = ""

        if minimum:
            query += "size >= \"{}\"".format(minimum)
        if minimum and maximum:
            query += " and "
        if maximum:
            query += "size <= \"{}\"".format(maximum)

        return query


class FileComponent(Component):
    projections = ["id", "name"]


class ContainerComponent(Component):
    projections = ["id", "name"]


class NoteComponent(Component):
    projections = ["note_id", "component_id", "component"]


class Project(Entity):
    projections = ["id", "name"]

    @Criteria.supported_targets(Entity)
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")

    @Criteria.supported_targets()
    def by_status(self, target, status):
        return "status like {}".format(status)

    # TODO - refactor, other entities use this too
    @Criteria.supported_targets()
    def by_lifespan(self, target, start=None, end=None):
        query = ""
        if target:
            implicit_target = "{}.".format(target.relation)
        else:
            implicit_target = ""

        if start:
            query += "{}start_date >= \"{}\"".format(implicit_target, start)
        if start and end:
            query += " and "
        if end:
            query += "{}end_date <= \"{}\"".format(implicit_target, end)

        return query

    def pre_create(self, **kwargs):
        super(Project, self).pre_create(**kwargs)

        session = kwargs.get("session")
        assert "project_schema" in kwargs, "project_schema is a required keyword argument"
        assert "name" in kwargs, "name is a required keyword argument"
        assert kwargs["project_schema"] in PROJECT_SCHEMAS.get("types", session), \
            "Unknown project_schema '{}'. Known schemas: {}".format(
                kwargs["project_schema"], ", ".join(PROJECT_SCHEMAS.get("types", session).keys())
            )

        kwargs["project_schema"] = PROJECT_SCHEMAS.get(kwargs["project_schema"], session)
        kwargs["no_parent"] = True
        if "full_name" not in kwargs:
            kwargs["full_name"] = kwargs["name"]
        return kwargs

    def create(self, name, project_schema, **kwargs): pass


class ComponentLocation(Entity):
    projections = ["id", "resource_identifier"]

    relationship = Relationship()
    relationship.parent = "component"

    def pre_create(self, **kwargs):
        super(ComponentLocation, self).pre_create(**kwargs)

        if "location" in kwargs:
            kwargs["location"] = list(kwargs["location"].values())[0].ftrack_entity
        else:
            kwargs.setdefault("location_id", "cb268ecc-8809-11e3-a7e2-20c9d081909b")  # unmanaged location

        assert "resource_identifier" in kwargs, "resource_identifier is a required keyword argument"
        return kwargs

    @Criteria.supported_targets(Entity)
    def by_name(self, target, *names):
        target = target or TargetRelation("location")
        return build_partial_query(target, names, "name")

    @Criteria.supported_targets(AssetVersion)
    def by_version(self, target, *versions):
        target = target or self.relationship[AssetVersion]
        return build_partial_query(target, versions, "version")

    @Criteria.supported_targets()
    def by_resource_identifier(self, target, *resource_identifiers):
        target = target or TargetRelation()
        return build_partial_query(target, resource_identifiers, "resource_identifier")


class Asset(Entity):
    projections = ["id", "name"]

    relationship = Relationship()

    @Criteria.supported_targets(Entity)
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")

    @Criteria.supported_targets(TypedContext)
    def by_type(self, target, *types):
        target = target or TargetRelation()
        return build_partial_query(target, types, "type.name")

    def pre_create(self, **kwargs):
        """ pre process before create() call

        Validates and modifies passed keyword arguments from create()

        Args:
            **kwargs (): incoming keyword arguments from create(**kwargs)

        Returns:

        """
        super(Asset, self).pre_create(**kwargs)

        session = kwargs["session"]
        assert "type" in kwargs, "asset_type is a required keyword argument"
        assert "name" in kwargs, "name is a required keyword argument"
        assert kwargs["type"] in ASSET_TYPES.get("types", session), \
            "Unknown asset_type '{}'. Known types: {}".format(kwargs["type"], ", ".join(ASSET_TYPES.get("types", session).keys()))
        kwargs["type"] = ASSET_TYPES.get(kwargs["type"], session)
        return kwargs

    # only for autocompletion
    def create(self, name, type, **kwargs): pass


class Status(Entity):
    projections = ["id", "name"]

    relationship = Relationship()

    # TODO: This needs proper target support; possible targets -> State, Status
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")


class State(Entity):
    projections = ["id", "name"]

    relationship = Relationship()


class AssetVersionLink(Entity):
    projections = ["id", "from_id", "to_id"]


class ProjectSchema(Entity):
    projections = ["id", "name"]


class User(Entity):
    projections = ["id", "username", "is_active"]

    relationship = Relationship()

    @Criteria.supported_targets()
    def by_active_state(self, target, *states):
        target = target or TargetRelation()
        return build_partial_query(target, states, "is_active")

    @Criteria.supported_targets(Entity)
    def by_name(self, target, *names):
        if not target:
            target = TargetRelation()
            return build_partial_query(target, names, "username")
        else:
            return build_partial_query(target, names, "name")


class Timelog(Entity):
    projections =["id", "comment", "start", "duration"]

    relationship = Relationship()
    relationship.parent = "user"

    @Criteria.supported_targets(User, Project)
    def by_name(self, target, *names):
        target = target or TargetRelation()
        if target is self.relationship[User]:
            return build_partial_query(target, names, "username")
        else:
            return build_partial_query(target, names, "name")

    @Criteria.supported_targets()
    def by_lifespan(self, target, start=None, end=None):
        if start:
            query = "start >= \"{}\"".format(start)
        if start and end:
            duration = int((end - start).total_seconds())
            query += " and duration <= \"{}\"".format(duration)
        if end and not start:
            pass

        return query


class UserSecurityRole(Entity):
    projections = ["id", "security_role", "projects"]


class UserSecurityRoleProject(Entity):
    projections = ["id", "project"]


class SecurityRole(Entity):
    projections = ["id", "name", "type"]


class Appointment(Entity):
    projections = ["id", "resource", "resource.name"]

    relationship = Relationship()
    relationship.parent = "context"

    def pre_create(self, **kwargs):
        super(Appointment, self).pre_create(**kwargs)
        kwargs.setdefault("type", "assignment")

        if kwargs.get("resource"):
            assert isinstance(kwargs["resource"], EntityCollection), \
                "Argument 'resource' expects a value of EntityCollection[User]"
            assert len(kwargs["resource"]) == 1, "'resource' can only be an EntityCollection with one entity."

            kwargs["resource"] = list(kwargs["resource"].values())[0].ftrack_entity

        return kwargs


class ObjectType(Entity):
    projections = ["id"]


class Context(Entity):
    projections = ["id"]


class AssetType(Entity):
    projections = ["id", "name"]


class Event(Entity):
    projections = ["id", "action", "user", "data"]

    relationship = Relationship()

    @Criteria.supported_targets(Entity)
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")

    @Criteria.supported_targets()
    def by_action(self, target, *actions):
        target = target or TargetRelation()
        return build_partial_query(target, actions, "action")

    @Criteria.supported_targets()
    def by_data(self, target, *datas):
        target = target or TargetRelation()
        return build_partial_query(target, datas, "data")


class TypedContextLink(Entity):
    projections = ["id", "from_id", "to_id"]


class TaskTypeSchema(Entity):
    projections = ["id", "types.name"]


class Type(Entity):
    projections = ["id", "name"]


class Metadata(Entity):
    projections = ["id", "key", "value"]


class NoteCategory(Entity):
    projections = ["id", "name"]

    @Criteria.supported_targets()
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")


class Note(Entity):
    projections = ["id", "content"]
    relationship = Relationship()

    # FIX: why do we need to set a parent if the precreate set
    #  the no_parent flag?
    relationship.parent = "parent_id"

    def pre_create(self, **kwargs):
        super(Note, self).pre_create(**kwargs)
        # assert "recipients" in kwargs, "recipients is a required keyword argument"

        author = kwargs.get("author")
        if author:
            assert isinstance(author, EntityCollection) and len(author) == 1,\
                "`author` must be a single element EntityCollection."
            author = list(author.values())[0]
            assert isinstance(author, User), "`author` collection must contain an element of type User."
            kwargs["author"] = author.ftrack_entity

        category = kwargs.get("category")
        if category:
            assert isinstance(category, EntityCollection) and len(category) == 1, \
                "`category` must be a single element EntityCollection."
            category = list(category.values())[0]
            # Querying a NodeCategory trough the Ftrack API returns a
            # dynamic NoteLabel class, hence this type is also valid
            assert isinstance(category, (NoteCategory, NoteLabel)), \
                "`category` collection must contain an element of type NoteCategory or NoteLabel."
            kwargs["category"] = category.ftrack_entity

        recipients = kwargs.get("recipients")
        if recipients:
            if isinstance(recipients, EntityCollection):
                if recipients.entity_type == User:
                    kwargs["recipient_resource_ids"] = recipients.id
                    kwargs["recipients"] = []
                elif recipients.entity_type == Recipient:
                    kwargs["recipients"] = [_.ftrack_entity for _ in recipients.values()]
                else:
                    raise NotImplementedError(
                        "We can only handle EntityCollection[User] or EntityCollection[Recipient] as recipients."
                    )
            else:
                raise AssertionError("`recipients`must be of type EntityCollection.")
        else:
            # TODO: handle replies??
            pass

        kwargs["no_parent"] = True
        return kwargs

    @Criteria.supported_targets(User, NoteCategory)
    def by_name(self, target, *names):
        target = target or TargetRelation()
        if target is self.relationship[User]:
            return build_partial_query(target, names, "username")
        return build_partial_query(target, names, "name")

    @Criteria.supported_targets(Entity)
    def by_id(self, target, *ids):
        # TODO: does not support the usual type-check for "parent" targets
        # TODO: check against type 'TypedContext' (+AssetVersion / Project? )
        if target and target.relation.startswith('parent['):
            query = "parent_id in ({})".format(", ".join(ids))
            # TODO: enable when ftrack api supports the query for "parent_type":
            # query += " and parent_type is {}".format(target.relation.split("[")[1].rstrip("]"))
            return query
        return super(Note, self).by_id(target, *ids)


class ReviewSession(Entity):
    projections = ["id", "name"]
    relationship = Relationship()

    def pre_create(self, **kwargs):
        super(ReviewSession, self).pre_create(**kwargs)

        assert "name" in kwargs, "name is a required keyword argument"
        assert "project" in kwargs, "project is a required keyword argument"
        kwargs["no_parent"] = True
        return kwargs

    def create(self, name, project_schema, **kwargs): pass

    @Criteria.supported_targets(Entity)
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")


class ReviewSessionObject(Entity):
    projections = ["id", "name"]
    relationship = Relationship()
    relationship.parent = "review_session"

    def pre_create(self, **kwargs):
        super(ReviewSessionObject, self).pre_create(**kwargs)

        if "asset_version" in kwargs:
            assert isinstance(kwargs["asset_version"], EntityCollection), "Argument 'asset_version' expects a value of EntityCollection[AssetVersion]"
            kwargs["asset_version"] = list(kwargs["asset_version"].values())[0].ftrack_entity
        return kwargs


class ReviewSessionInvitee(Entity):
    projections = ["id", "name", "email"]
    relationship = Relationship()
    # TEST: Check if this is needed or how it is actually used.
    relationship.parent = "review_session"

    def pre_create(self, **kwargs):
        super(ReviewSessionInvitee, self).pre_create(**kwargs)
        return kwargs


class ReviewSessionObjectStatus(Entity):
    projections = ["id", "status"]


class Recipient(Entity):
    # recipients are only used in notes and thus we can simply project
    # everything
    projections = ["resource_id", "note", "note_id", "recipient", "user"]

    relationship = Relationship()


class EntitySetting(Entity):
    pass


class Group(Entity):
    projections = ["id", "name"]

    @Criteria.supported_targets()
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")


class Job(Entity):
    projections = ["id", "status", "data"]

    relationship = Relationship()

    @Criteria.supported_targets(Entity)
    def by_name(self, target, *names):
        if not target:
            query = "("
            for name in names:
                query += "(data any (key is name and value like \"{}\")) or ".format(name)
            query = query[:-4] + ")"
        elif target is self.relationship[User]:
            query = build_partial_query(target, names, "username")
        else:
            query = build_partial_query(target, names, "name")
        return query

    @Criteria.supported_targets()
    def by_data(self, target, *dictionaries):
        query = "("
        for _dict in dictionaries:
            query += "("
            for key, value in _dict.items():
                if target:
                    query += "{}.".format(target.relation)
                query += "data any (key like \"{}\" and value like \"{}\") and ".format(key, value)
            query = query[:-5] + ") or "
        query = query[:-4] + ")"
        return query

    @Criteria.supported_targets()
    def by_status(self, target, *status):
        target = target or TargetRelation()
        return build_partial_query(target, status, "status")

    @Criteria.supported_targets()
    def by_lifespan(self, target, start=None, end=None):
        query = ""
        if target:
            implicit_target = "{}.".format(target.relation)
        else:
            implicit_target = ""

        if start:
            query += "{}created_at >= \"{}\"".format(implicit_target, start)
        if start and end:
            query += " and "
        if end:
            query += "{}finished_at <= \"{}\"".format(implicit_target, end)

        return query

    @Criteria.supported_targets()
    def by_creation_date(self, target, creation_date):
        query = ""
        if target:
            implicit_target = "{}.".format(target.relation)
        else:
            implicit_target = ""

        query += "{}created_at like \"{}%\"".format(implicit_target, creation_date.format("YYYY-MM-DD"))

        return query

    @Criteria.supported_targets()
    def by_finish_date(self, target, finish_date):
        query = ""
        if target:
            implicit_target = "{}.".format(target.relation)
        else:
            implicit_target = ""

        query += "{}finished_at like \"{}%\"".format(implicit_target, finish_date.format("YYYY-MM-DD"))

        return query


class Membership(Entity):
    projections = ["id", "group"]


class Location(Entity):
    projections = ["id", "name"]

    @Criteria.supported_targets()
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")


class List(Entity):
    projections = ["id", "name"]

    relationship = Relationship()

    @Criteria.supported_targets(Project, ListCategory)
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")


class TypedContextList(List):
    pass


class AssetVersionList(List):

    def pre_create(self, **kwargs):
        """ pre process before create() call

        Validates and modifies passed keyword arguments from create()

        Args:
            **kwargs (): incoming keyword arguments from create(**kwargs)

        Returns:

        """
        super(AssetVersionList, self).pre_create(**kwargs)

        assert "project" in kwargs, "project is a required keyword argument"
        assert len(kwargs["project"]) == 1, "Only one project can be linked to an AssetVersionList. You provided {}.".format(
            len(kwargs["project"])
        )
        assert isinstance(kwargs["project"], EntityCollection), "Argument 'project' expects a value of EntityCollection[Project]"

        kwargs["project"] = list(kwargs["project"].values())[0].ftrack_entity

        assert "category" in kwargs, "category is a required keyword argument"
        assert len(kwargs["category"]) == 1, "Only one category can be linked to an AssetVersionList. You provided {}.".format(
            len(kwargs["category"])
        )
        assert isinstance(kwargs["category"], EntityCollection), "Argument 'category' expects a value of EntityCollection[ListCategory]"

        kwargs["category"] = list(kwargs["category"].values())[0].ftrack_entity

        return kwargs

    # only for autocompletion
    def create(self, task, **kwargs): pass


class ListCategory(Entity):
    projections = ["id", "name"]

    relationship = Relationship()

    @Criteria.supported_targets()
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")


class WorkflowSchema(Entity):
    pass


class NoteLabel(Entity):
    projections = ["id", "name"]

    @Criteria.supported_targets(Entity)
    def by_name(self, target, *names):
        target = target or TargetRelation()
        return build_partial_query(target, names, "name")


class Resource(Entity):
    pass


# automatically declare classes for all TypedContext objects
for _type in OBJECT_TYPES.types:
    if _type not in locals() or issubclass(locals().get(_type, None), ForwardDeclaration):
        locals()[_type] = type(str(_type), (TypedContext,), {"projections": ['id', 'name']})
