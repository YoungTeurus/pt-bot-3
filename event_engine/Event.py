from abc import ABC, abstractmethod

DEFAULT_PRIORITY = 5
EVENT_TYPE = str


class Event(ABC):
    priority: int
    type: EVENT_TYPE
    args: list[object]

    def __init__(self, args: list[object], priority: int = DEFAULT_PRIORITY, type: EVENT_TYPE | None = None):
        self.priority = priority
        self.type = type if type is not None else self.__class__.__name__
        self.args = args

    @abstractmethod
    def _getArgsDescription(self) -> list[tuple[str, type]]:
        raise NotImplemented

    def __str__(self):
        return f"{Event.__name__}{{priority={self.priority},type={self.type},args={self.args}}}"

    def __lt__(self, other):
        if not isinstance(other, Event):
            raise TypeError
        return self.priority < other.priority
