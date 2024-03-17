from abc import ABC, abstractmethod

from event_engine.Event import Event


class EventConsumer(ABC):
    __consumableEventTypes: set[str]
    __consuming: bool

    def __init__(self, consumableEventTypes: list[str], consuming: bool):
        self.__consumableEventTypes = set(consumableEventTypes)
        self.__consuming = consuming

    def consume(self, event: Event) -> Event | None:
        if event.type not in self.__consumableEventTypes:
            return event

        self._doConsume(event)

        if self.__consuming:
            return None
        return event

    @abstractmethod
    def _doConsume(self, event: Event) -> None:
        raise NotImplemented()
