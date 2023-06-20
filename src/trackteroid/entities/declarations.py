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

import itertools
import importlib
import inspect
import logging
import re


from ..configuration import LOGGING_NAMESPACE


_LOG = logging.getLogger("{}.declarations".format(LOGGING_NAMESPACE))


class ForwardDeclaration:
    pass


class RelationshipDeclaration:
    """ a declaration for a used relationship that needs resolution

    """
    def __init__(self, parent, child):
        self._filter_re = re.compile("\[\w+\]")
        self._chain = []
        self._entities_module = importlib.import_module("..entities", __name__)
        self._chain.extend(
            [
                getattr(self._entities_module, parent.__name__, parent),
                getattr(self._entities_module, child.__name__ if not isinstance(child, str) else child, child)
            ]
        )

    def __getattr__(self, item):
        # TODO: what requests `shape`??
        if not item.startswith("__") and item != "shape":
            self._chain.append(getattr(self._entities_module, item, item))
        return self

    def resolve_path_for(self, entity_type, session, schema):
        relationships = []
        for item in self._chain:
            if item:
                if not isinstance(item, str):
                    item.relationship(session=session, schema=schema)
                    relationship = entity_type.relationship.get(item)
                    if not relationship:
                        _LOG.warning(
                            "Unable to retrieve relationship between target entity type `{}` and entity type `{}`."
                            "You should consider providing via the configurable `RELATIONSHIP_RESOLVER`.".format(
                                entity_type.__class__.__name__,
                                item.__name__
                            )
                        )
                        continue
                    if not isinstance(relationship.relation, list):
                        relationships.append([self._filter_re.sub("", relationship.relation)])
                    else:
                        relationships.append(
                            [self._filter_re.sub("", _) for _ in relationship.relation]
                        )
                    entity_type = item
                else:
                    relationships.append([item])

        return [".".join(_) for _ in itertools.product(*relationships)]


class ForwardDeclareCompare(type):
    def __eq__(self, other):
        if other and inspect.isclass(other) and issubclass(other, ForwardDeclaration):
            return self.__name__ == other.__name__
        else:
            return super(ForwardDeclareCompare, self).__eq__(other)

    def __ne__(self, other):
        return not self == other

    def __getattr__(self, item):
        return RelationshipDeclaration(parent=self, child=item)

    def __hash__(self):
        return hash(self.__class__.__name__)


# TODO: we need to auto-regenerate this when the schema changes
class Appointment(ForwardDeclaration): pass
class Asset(ForwardDeclaration): pass
class AssetBuild(ForwardDeclaration): pass
class AssetCustomAttributeLink(ForwardDeclaration): pass
class AssetCustomAttributeLinkFrom(ForwardDeclaration): pass
class AssetCustomAttributeValue(ForwardDeclaration): pass
class AssetGroup(ForwardDeclaration): pass
class AssetType(ForwardDeclaration): pass
class AssetVersion(ForwardDeclaration): pass
class AssetVersionCustomAttributeLink(ForwardDeclaration): pass
class AssetVersionCustomAttributeLinkFrom(ForwardDeclaration): pass
class AssetVersionCustomAttributeValue(ForwardDeclaration): pass
class AssetVersionLink(ForwardDeclaration): pass
class AssetVersionList(ForwardDeclaration): pass
class AssetVersionStatusChange(ForwardDeclaration): pass
class CalendarEvent(ForwardDeclaration): pass
class CalendarEventResource(ForwardDeclaration): pass
class Component(ForwardDeclaration): pass
class ComponentCustomAttributeLink(ForwardDeclaration): pass
class ComponentCustomAttributeLinkFrom(ForwardDeclaration): pass
class ComponentLocation(ForwardDeclaration): pass
class ContainerComponent(ForwardDeclaration): pass
class Context(ForwardDeclaration): pass
class ContextCustomAttributeLink(ForwardDeclaration): pass
class ContextCustomAttributeLinkFrom(ForwardDeclaration): pass
class ContextCustomAttributeValue(ForwardDeclaration): pass
class Conversation(ForwardDeclaration): pass
class CustomAttributeConfiguration(ForwardDeclaration): pass
class CustomAttributeGroup(ForwardDeclaration): pass
class CustomAttributeLink(ForwardDeclaration): pass
class CustomAttributeLinkConfiguration(ForwardDeclaration): pass
class CustomAttributeLinkFrom(ForwardDeclaration): pass
class CustomAttributeType(ForwardDeclaration): pass
class CustomAttributeValue(ForwardDeclaration): pass
class CustomConfigurationBase(ForwardDeclaration): pass
class Dashboard(ForwardDeclaration): pass
class DashboardResource(ForwardDeclaration): pass
class DashboardWidget(ForwardDeclaration): pass
class Disk(ForwardDeclaration): pass
class EntitySetting(ForwardDeclaration): pass
class Epic(ForwardDeclaration): pass
class Episode(ForwardDeclaration): pass
class Event(ForwardDeclaration): pass
class Feed(ForwardDeclaration): pass
class FileComponent(ForwardDeclaration): pass
class Floor(ForwardDeclaration): pass
class Folder(ForwardDeclaration): pass
class Group(ForwardDeclaration): pass
class GroupCustomAttributeLink(ForwardDeclaration): pass
class GroupCustomAttributeLinkFrom(ForwardDeclaration): pass
class Hardware(ForwardDeclaration): pass
class Job(ForwardDeclaration): pass
class JobComponent(ForwardDeclaration): pass
class License(ForwardDeclaration): pass
class List(ForwardDeclaration): pass
class ListCategory(ForwardDeclaration): pass
class ListCustomAttributeLink(ForwardDeclaration): pass
class ListCustomAttributeLinkFrom(ForwardDeclaration): pass
class ListCustomAttributeValue(ForwardDeclaration): pass
class ListObject(ForwardDeclaration): pass
class ListObjectCustomAttributeValue(ForwardDeclaration): pass
class Location(ForwardDeclaration): pass
class Manager(ForwardDeclaration): pass
class ManagerType(ForwardDeclaration): pass
class Membership(ForwardDeclaration): pass
class Message(ForwardDeclaration): pass
class Metadata(ForwardDeclaration): pass
class Milestone(ForwardDeclaration): pass
class Note(ForwardDeclaration): pass
class NoteCategory(ForwardDeclaration): pass
class NoteComponent(ForwardDeclaration): pass
class NoteLabel(ForwardDeclaration): pass
class NoteLabelLink(ForwardDeclaration): pass
class ObjectType(ForwardDeclaration): pass
class Office(ForwardDeclaration): pass
class Participant(ForwardDeclaration): pass
class Priority(ForwardDeclaration): pass
class Project(ForwardDeclaration): pass
class ProjectSchema(ForwardDeclaration): pass
class ProjectSchemaObjectType(ForwardDeclaration): pass
class ProjectSchemaOverride(ForwardDeclaration): pass
class Recipient(ForwardDeclaration): pass
class Resource(ForwardDeclaration): pass
class Resources(ForwardDeclaration): pass
class ReviewSession(ForwardDeclaration): pass
class ReviewSessionInvitee(ForwardDeclaration): pass
class ReviewSessionObject(ForwardDeclaration): pass
class ReviewSessionObjectStatus(ForwardDeclaration): pass
class Schema(ForwardDeclaration): pass
class SchemaStatus(ForwardDeclaration): pass
class SchemaType(ForwardDeclaration): pass
class Scope(ForwardDeclaration): pass
class Seat(ForwardDeclaration): pass
class SecurityRole(ForwardDeclaration): pass
class Sequence(ForwardDeclaration): pass
class SequenceComponent(ForwardDeclaration): pass
class Setting(ForwardDeclaration): pass
class SettingComponent(ForwardDeclaration): pass
class Shot(ForwardDeclaration): pass
class Sprint(ForwardDeclaration): pass
class State(ForwardDeclaration): pass
class Status(ForwardDeclaration): pass
class StatusChange(ForwardDeclaration): pass
class Task(ForwardDeclaration): pass
class TaskTemplate(ForwardDeclaration): pass
class TaskTemplateItem(ForwardDeclaration): pass
class TaskTypeSchema(ForwardDeclaration): pass
class TaskTypeSchemaType(ForwardDeclaration): pass
class TestTest(ForwardDeclaration): pass
class Timelog(ForwardDeclaration): pass
class Timer(ForwardDeclaration): pass
class Type(ForwardDeclaration): pass
class TypedContext(ForwardDeclaration): pass
class TypedContextLink(ForwardDeclaration): pass
class TypedContextList(ForwardDeclaration): pass
class TypedContextStatusChange(ForwardDeclaration): pass
class User(ForwardDeclaration): pass
class UserApplicationState(ForwardDeclaration): pass
class UserCustomAttributeLink(ForwardDeclaration): pass
class UserCustomAttributeLinkFrom(ForwardDeclaration): pass
class UserCustomAttributeValue(ForwardDeclaration): pass
class UserSecurityRole(ForwardDeclaration): pass
class UserSecurityRoleProject(ForwardDeclaration): pass
class UserType(ForwardDeclaration): pass
class WorkflowSchema(ForwardDeclaration): pass
class WorkflowSchemaStatus(ForwardDeclaration): pass