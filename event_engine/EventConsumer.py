from abc import ABC, abstractmethod

from event_engine.Event import Event


class EventConsumer(ABC):
    __consumableEventTypes: set[str]

    def __init__(self, consumableEventTypes: list[str]):
        self.__consumableEventTypes = set(consumableEventTypes)

    def consume(self, event: Event) -> tuple[bool, Event | None]:
        if event.eType not in self.__consumableEventTypes:
            return False, event

        return True, self._doConsume(event)

    @abstractmethod
    def _doConsume(self, event: Event) -> Event | None:
        raise NotImplemented()

    def _name(self) -> str:
        return f"{self.__class__.__name__}"

    def __str__(self) -> str:
        return f"{self._name()}:{self.__consumableEventTypes}"
