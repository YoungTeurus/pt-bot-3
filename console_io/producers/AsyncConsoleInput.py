from asyncio import AbstractEventLoop

from aioconsole import ainput

from console_io.events.SimpleMessageEvent import SimpleMessageEvent
from event_engine.EventProcessor import EventProcessor


class AsyncConsoleInput:
    __running: bool
    __proc: EventProcessor

    def __init__(self, proc: EventProcessor):
        self.__running = False
        self.__proc = proc

    def start(self, eventLoop: AbstractEventLoop) -> None:
        self.__running = True
        eventLoop.run_until_complete(self.__run())

    def stop(self) -> None:
        self.__running = False

    async def __run(self):
        while self.__running:
            msg = await ainput('>')
            self.__proc.push(SimpleMessageEvent(msg))
