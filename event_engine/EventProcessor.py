from queue import PriorityQueue, Empty
from threading import Thread
from typing import Callable

from event_engine.Event import Event
from event_engine.EventConsumer import EventConsumer
from modules.console_io.ConsoleOutputter import ConsoleOutputter


class EventProcessor:
    __eventQueue: PriorityQueue
    __eventConsumers: list[EventConsumer]
    __consumersToRemove: list[EventConsumer]
    __thread: Thread
    __running: bool
    debugEventProcessing: bool
    debugEventConsuming: bool
    debugConsumersRemoving: bool

    def __init__(self):
        self.__eventQueue = PriorityQueue()
        self.__eventConsumers = []
        self.__consumersToRemove = []
        self.__running = False
        self.__thread = Thread(target=self.__mainCycle, name="EventProcessor thread")
        self.debugEventProcessing = False
        self.debugEventConsuming = False
        self.debugConsumersRemoving = False

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
        return lambda: self.__consumersToRemove.append(consumer)

    def __mainCycle(self) -> None:
        while self.__running:
            self.__removeConsumers()
            self.__tryProcessNextEvent()

    def __removeConsumers(self):
        for consumer in self.__consumersToRemove:
            if self.debugConsumersRemoving:
                ConsoleOutputter.toConsole(f"Consumer {consumer} was removed")
            self.__eventConsumers.remove(consumer)
        self.__consumersToRemove = []

    def __tryProcessNextEvent(self) -> None:
        try:
            event = self.__eventQueue.get(timeout=0.2)
        except Empty:
            return

        if self.debugEventProcessing:
            ConsoleOutputter.toConsole(f"Processing {event}")

        for consumer in self.__eventConsumers:
            if event is None:
                return
            isProcessed, event = consumer.consume(event)

            if self.debugEventProcessing and isProcessed:
                ConsoleOutputter.toConsole(
                    f"Event was processed by {consumer}")
            if self.debugEventConsuming and event is None:
                ConsoleOutputter.toConsole(f"Event was consumed by {consumer}")
