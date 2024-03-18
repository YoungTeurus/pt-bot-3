from selenium.webdriver.chromium.webdriver import ChromiumDriver

from modules.browser.rountines.Routine import Routine


class LoadInPT(Routine):
    def _do(self, driver: ChromiumDriver, args: list) -> None:
        driver.get("https://pony.town/")
