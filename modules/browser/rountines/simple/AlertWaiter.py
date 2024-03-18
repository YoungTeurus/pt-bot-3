from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from event_engine.Event import EVENT_ARGS_DESCRIPTION
from modules.browser.rountines.Routine import Routine


class AlertWaiter(Routine):
    """
    Проверяет, что сейчас открыт какой-либо Alert, и ждёт его закрытия.
    """

    def _getStartArgsDescription(self) -> EVENT_ARGS_DESCRIPTION:
        return [
            ("Таймаут ожидания", float | None)
        ]

    def _do(self, driver: ChromiumDriver, args: list) -> None:
        timeout = args[0] if args else 10
        WebDriverWait(driver, timeout).until_not(EC.alert_is_present())

if __name__ == "__main__":
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    driver.get("http://ya.ru")

    driver.execute_script("alert(1)")
    WebDriverWait(driver, 3).until_not(EC.alert_is_present())
    driver.get("http://google.com")

    while True:
        pass