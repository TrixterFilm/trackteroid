from typing import *
from ..session import Session

T = TypeVar('T')

class Query(Generic[T]):
    _known_order: ClassVar[List[str]] = ["ascending", "descending"]

    def __new__(cls: Type[Query[T]], _cls: T, session: Optional[Session], schema: Optional[dict]) -> T: ...