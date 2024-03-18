from selenium.webdriver.chromium.webdriver import ChromiumDriver

from event_engine.Event import Event, EVENT_ARGS_DESCRIPTION


class BrowserLoadedEvent(Event):
    def _getArgsDescription(self) -> EVENT_ARGS_DESCRIPTION:
        return [
            ("Browser driver", ChromiumDriver)
        ]
