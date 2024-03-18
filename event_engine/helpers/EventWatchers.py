from typing import Callable

from event_engine.Event import EVENT_TYPE, Event
from event_engine.EventConsumer import EventConsumer
from event_engine.EventProcessor import EventProcessor


def doOnceEvent(proc: EventProcessor, type: EVENT_TYPE, action: Callable[[Event], Event | None],
                eventArgs: list | None = None):
    class ConsumeOnceConsumer(EventConsumer):
        def __init__(self):
            super().__init__([type])
            self.__destroy = proc.addConsumer(self)

        def _doConsume(self, event: Event) -> Event | None:
            if eventArgs is not None and event.args != eventArgs:
                return event
            self.__destroy()
            return action(event)

    return ConsumeOnceConsumer()
