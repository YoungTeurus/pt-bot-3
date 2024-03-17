from abc import ABC, abstractmethod
from dataclasses import dataclass, field

DEFAULT_PRIORITY = 5


@dataclass(order=True)
class Event(ABC):
    priority: int
    type: str = field(compare=False)
    args: list[object] = field(compare=False)

    def __init__(self, type: str, args: list[object], priority: int = DEFAULT_PRIORITY):
        self.priority = priority
        self.type = type
        self.args = args

    @abstractmethod
    def _getArgsDescription(self) -> list[str]:
        raise NotImplemented