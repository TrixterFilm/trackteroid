from typing import *
from ..session import Session

T = TypeVar('T')

class Query(object):
    _known_order: ClassVar[List[str]] = ["ascending", "descending"]

    def __new__(cls: Query, _cls: T, session: Optional[Session], schema: Optional[dict], *args: Any, select: List[str], **kwargs: Any) -> T: ...

