from abc import ABC, abstractmethod
from types import UnionType

DEFAULT_PRIORITY = 5
EVENT_TYPE = str
EVENT_ARGS_DESCRIPTION = list[tuple[str, type | UnionType]]


class Event(ABC):
    __priority: int
    eType: EVENT_TYPE
    args: list[object]

    def __init__(self, args: list[object], priority: int = DEFAULT_PRIORITY, type: EVENT_TYPE | None = None):
        self.__priority = priority
        self.eType = type if type is not None else self.__class__.__name__
        self.args = args

    @abstractmethod
    def _getArgsDescription(self) -> EVENT_ARGS_DESCRIPTION:
        raise NotImplemented

    def __str__(self):
        return f"{Event.__name__}{{priority={self.__priority},type={self.eType},args={self.args}}}"

    def __lt__(self, other):
        if not isinstance(other, Event):
            raise TypeError
        return self.__priority < other.__priority
