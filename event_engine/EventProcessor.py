from queue import PriorityQueue, Empty
from threading import Thread
from typing import Callable

from console_io.ConsoleOutputter import ConsoleOutputter
from event_engine.Event import Event
from event_engine.EventConsumer import EventConsumer


class EventProcessor:
    __eventQueue: PriorityQueue
    __eventConsumers: list[EventConsumer]
    __thread: Thread
    __running: bool
    __debugAllEvents: bool

    def __init__(self, debugAllEvents: bool = False):
        self.__eventQueue = PriorityQueue()
        self.__eventConsumers = []
        self.__running = False
        self.__thread = Thread(target=self.__mainCycle, name="EventProcessor thread")
        self.__debugAllEvents = debugAllEvents

    def start(self) -> None:
        self.__running = True
        self.__thread.start()

    def stop(self) -> None:
        self.__running = False
        self.__thread.join(5)

    def push(self, event: Event) -> None:
        self.__eventQueue.put(event)

    def addConsumer(self, consumer: EventConsumer) -> Callable[[], None]:
        self.__eventConsumers.append(consumer)
        return lambda: self.__eventConsumers.remove(consumer)

    def __mainCycle(self) -> None:
        while self.__running:
            try:
                event = self.__eventQueue.get(timeout=0.2)
                if self.__debugAllEvents:
                    ConsoleOutputter.toConsole(f"Processing {event}")
                for consumer in self.__eventConsumers:
                    if event is None:
                        continue
                    event = consumer.consume(event)
            except Empty:
                continue
