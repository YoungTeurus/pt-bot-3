from typing import Callable
from uuid import uuid4

from event_engine.Event import EVENT_TYPE, Event, DEFAULT_PRIORITY, EVENT_ARGS_DESCRIPTION
from event_engine.EventConsumer import EventConsumer
from event_engine.EventProcessor import EventProcessor


def doOnceEvent(proc: EventProcessor, type: EVENT_TYPE, action: Callable[[Event], Event | None],
                eventArgs: list | None = None, consumerName: str | None = None) -> None:
    class ConsumeOnceConsumer(EventConsumer):
        def __init__(self):
            super().__init__([type])
            self.__destroy = proc.addConsumer(self)

        def _name(self) -> str:
            return ConsumeOnceConsumer.__name__ if consumerName is None else consumerName

        def _doConsume(self, event: Event) -> Event | None:
            if eventArgs is not None and event.args != eventArgs:
                return event
            self.__destroy()
            return action(event)

    ConsumeOnceConsumer()


def doInChain(proc: EventProcessor, calls: list[Callable[[], None]]) -> None:
    chainUuid = uuid4()
    chainEventType = f"Chain-{chainUuid}"

    class ChainStartNextEvent(Event):
        def __init__(self, args: list[object]):
            super().__init__(args, DEFAULT_PRIORITY, f"Chain-{chainUuid}")

        def _getArgsDescription(self) -> EVENT_ARGS_DESCRIPTION:
            return [
                ("Номер вызываемого элемента из серии", int)
            ]

    def process(callIndex: int) -> None:
        calls[callIndex]()
        proc.push(ChainStartNextEvent([callIndex + 1]))

    for i, call in enumerate(calls):
        doOnceEvent(proc, chainEventType, lambda e: process(e.args[0]),
                    eventArgs=[i],
                    consumerName=f"chain-{chainUuid}-{i}")
    proc.push(ChainStartNextEvent([0]))


def __test_doInChain():
    proc = EventProcessor()
    proc.debugEventProcessing = True
    proc.debugEventConsuming = True
    proc.debugConsumersRemoving = True

    proc.start()
    running = [True]

    def stop():
        running[0] = False

    doInChain(proc, [
        lambda: print("The first"),
        lambda: print("The second"),
        lambda: print("The last"),
        stop,
    ])

    while running[0]:
        pass
    print("Stopping")
    proc.stop()


if __name__ == "__main__":
    # __test_doInChain()
    pass
