from abc import ABC, abstractmethod
from threading import Thread

from selenium.webdriver.chromium.webdriver import ChromiumDriver

from event_engine.Event import EVENT_ARGS_DESCRIPTION
from event_engine.EventProcessor import EventProcessor
from modules.browser.rountines.RoutineEndEvent import RoutineEndEvent
from modules.browser.rountines.RoutineStartEvent import RoutineStartEvent


class Routine(ABC):
    def __init__(self, proc: EventProcessor, name: str | None = None):
        self.__proc = proc
        self.__name = self.__class__.__name__ if name is None else name

    @abstractmethod
    def _getStartArgsDescription(self) -> EVENT_ARGS_DESCRIPTION:
        raise NotImplemented

    def start(self, driver: ChromiumDriver, args: list) -> None:
        Thread(target=self.__do(driver, args)).start()

    def __do(self, driver: ChromiumDriver, args: list) -> None:
        self.__proc.push(RoutineStartEvent(args))
        self._do(driver, args)
        self.__proc.push(RoutineEndEvent(args))

    @abstractmethod
    def _do(self, driver: ChromiumDriver, args: list) -> None:
        raise NotImplemented
