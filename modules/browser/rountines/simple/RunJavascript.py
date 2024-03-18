from selenium.webdriver.chromium.webdriver import ChromiumDriver

from event_engine.Event import EVENT_ARGS_DESCRIPTION
from modules.browser.rountines.Routine import Routine


class RunJavascript(Routine):
    def _getStartArgsDescription(self) -> EVENT_ARGS_DESCRIPTION:
        return [
            ("Code", str)
        ]

    def _do(self, driver: ChromiumDriver, args: list) -> None:
        driver.execute_script(args[0])
