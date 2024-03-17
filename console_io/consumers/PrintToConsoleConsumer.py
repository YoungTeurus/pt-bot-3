from console_io.events.SimpleMessageEvent import SimpleMessageEvent
from event_engine.Event import Event
from event_engine.EventConsumer import EventConsumer


class PrintToConsoleConsumer(EventConsumer):
    def __init__(self):
        super().__init__([SimpleMessageEvent.__name__], False)

    def _doConsume(self, event: Event) -> None:
        print(event.args[0])
