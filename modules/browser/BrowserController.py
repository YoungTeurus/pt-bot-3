from selenium import webdriver
from selenium.webdriver.chromium.webdriver import ChromiumDriver

from event_engine.EventProcessor import EventProcessor
from modules.browser.events.BrowserLoadedEvent import BrowserLoadedEvent


class BrowserController:
    __driver: ChromiumDriver | None

    def __init__(self, proc: EventProcessor):
        self.__proc = proc

    def start(self) -> None:
        self.__driver = webdriver.Chrome()
        self.__proc.push(BrowserLoadedEvent([self.__driver]))

    def stop(self) -> None:
        if self.__driver is not None:
            self.__driver.quit()
