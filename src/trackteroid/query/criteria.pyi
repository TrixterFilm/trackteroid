import datetime
import arrow
from typing import Optional, Union, Callable
from collections import namedtuple
from ..entities import Entity
from .query import Query

optional_time = Optional[Union[datetime.datetime, arrow.Arrow]]

Criterion: namedtuple

class Criteria:
    def by_id(self, *ids: int) -> Query: ...
    def by_location(self, *locations: object) -> Query: ...
    def by_path(self, *paths: str) -> Query: ...
    def by_version(self, *versions: int) -> Query: ...
    def by_name(self, *names: str) -> Query: ...
    def by_component(self, *components: str) -> Query: ...
    def by_status(self, *status: str) -> Query: ...
    def by_shot(self, *shots: str) -> Query: ...
    def by_sequence(self, *sequences: str) -> Query: ...
    def by_task(self, *tasks: str) -> Query: ...
    def by_type(self, *types: str) -> Query: ...
    def by_project(self, *projects: str) -> Query: ...
    def by_metadata(self, **dictionaries: str) -> Query: ...
    def by_description(self, regex: str) -> Query: ...
    def by_comment(self, regex: str) -> Query: ...
    def by_publisher(self, *publishers: str) -> Query: ...
    def by_assetgroup(self, *assetgroups: str) -> Query: ...
    def by_state(self, *states: str) -> Query: ...
    def by_list(self, *lists: str) -> Query: ...
    def by_publish_time(self, start: optional_time = None, end: optional_time = None) -> Query: ...
    def by_status_change_time(self, start: optional_time = None, end: optional_time = None) -> Query: ...
    def by_assignee(self, *assignees: str) -> Query: ...
    def by_lifespan(self, start: optional_time = None, end: optional_time = None) -> Query: ...
    def by_outgoing_link(self, *ids: str) -> Query: ...
    def by_incoming_link(self, *ids: str) -> Query: ...
    def inject(self, filter: str) -> Query: ...

    @staticmethod
    def supported_targets(*supported: Entity) -> Callable: ...