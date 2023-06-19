import typing

T = typing.TypeVar('T')

class Relationship(dict):
    def __setitem__(self, key: typing.Type['Entity'], value: str) -> None: ...
    def __getitem__(self, item: typing.Type['Entity']) -> str: ...

class Entity(object):
    relationship: Relationship = Relationship()

    def __new__(cls: Entity, _cls: T, *args: typing.Tuple[typing.Any], **kwargs: typing.Dict[str, typing.Any]) -> T: ...

    def get(
        self,
        limit: typing.Optional[int] = None,
        offset: int = 0,
        order: str = "ascending",
        order_by: typing.Optional[str] = None
    ) -> EntityCollection: ...
    def get_one(self) -> Entity: ...
    def get_first(self) -> Entity: ...
    def get_all(self) -> EntityCollection: ...
    def get_inputs(self) -> EntityCollection: ...
    def get_outputs(self) -> EntityCollection: ...

class EntityCollection(object):
    def __new__(cls: Entity, _cls: T, *args: typing.Tuple[typing.Any], **kwargs: typing.Dict[str, typing.Any]) -> T: ...

class EmptyCollection(object):
    pass