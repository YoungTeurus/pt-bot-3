from threading import Thread

from console_io.events.ConsoleInputEvent import ConsoleInputEvent
from event_engine.EventProcessor import EventProcessor


class AsyncConsoleInput:
    __running: bool
    __thread: Thread
    __proc: EventProcessor

    def __init__(self, proc: EventProcessor):
        self.__running = False
        self.__thread = Thread(target=self.__run, name="AsyncConsoleInput thread", daemon=True)
        self.__proc = proc

    def start(self) -> None:
        self.__running = True
        self.__thread.start()

    def stop(self) -> None:
        self.__running = False

    def __run(self):
        while self.__running:
            try:
                # fixme: При завершении работы приходится лишний раз нажимать Enter, т.к. input захватывает управление
                msg = input('>')
                self.__proc.push(ConsoleInputEvent(msg))
            except UnicodeDecodeError:
                pass
