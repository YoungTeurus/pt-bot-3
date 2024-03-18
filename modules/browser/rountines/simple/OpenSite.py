from selenium.webdriver.chromium.webdriver import ChromiumDriver

from event_engine.EventProcessor import EventProcessor
from modules.browser.rountines.Routine import Routine


class OpenSite(Routine):
    def _getStartArgsDescription(self) -> list[tuple[str, type]]:
        return [
            ("URL", str)
        ]

    def __init__(self, proc: EventProcessor):
        super().__init__(proc)

    def _do(self, driver: ChromiumDriver, args: list) -> None:
        driver.get(args[0])
