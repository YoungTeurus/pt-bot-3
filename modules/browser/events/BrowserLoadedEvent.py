from selenium.webdriver.chromium.webdriver import ChromiumDriver

from event_engine.Event import Event


class BrowserLoadedEvent(Event):
    def _getArgsDescription(self) -> list[tuple[str, type]]:
        return [
            ("Browser driver", ChromiumDriver)
        ]
