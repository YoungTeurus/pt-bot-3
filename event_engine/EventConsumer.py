from abc import ABC, abstractmethod

from event_engine.Event import Event


class EventConsumer(ABC):
    __consumableEventTypes: set[str]

    def __init__(self, consumableEventTypes: list[str]):
        self.__consumableEventTypes = set(consumableEventTypes)

    def consume(self, event: Event) -> Event | None:
        if event.type not in self.__consumableEventTypes:
            return event

        return self._doConsume(event)

    @abstractmethod
    def _doConsume(self, event: Event) -> Event | None:
        raise NotImplemented()
