from selenium.webdriver.chromium.webdriver import ChromiumDriver

from event_engine.Event import Event
from event_engine.EventProcessor import EventProcessor
from event_engine.helpers.EventWatchers import doOnceEvent, doInChain
from modules.browser.BrowserController import BrowserController
from modules.browser.events.BrowserLoadedEvent import BrowserLoadedEvent
from modules.browser.rountines.simple.AlertWaiter import AlertWaiter
from modules.browser.rountines.simple.OpenSite import OpenSite
from modules.browser.rountines.simple.RunJavascript import RunJavascript
from modules.comands.CommandDictionary import CommandDictionary
from modules.comands.CommandTypes import CommandSource
from modules.comands.console.ConsoleCommandProcessor import ConsoleCommandProcessor
from modules.console_io.ConsoleOutputter import ConsoleOutputter
from modules.console_io.producers.ConsoleInputer import AsyncConsoleInput

if __name__ == '__main__':
    proc = EventProcessor()
    proc.debugEventProcessing = True
    # proc.debugEventConsuming = True
    # proc.debugConsumersRemoving = True

    proc.start()

    # Пример: обработка сообщения один раз
    # doOnceEvent(proc, ConsoleInputEvent.__name__,
    #             lambda event: ConsoleOutputter.toConsole(event.args[0] + "ice"),
    #             eventArgs=["N"])

    # Работа с консолью
    aci = AsyncConsoleInput(proc)
    aci.start()

    # Работа с командами
    comDict = CommandDictionary()
    botRunning = [True]
    proc.addConsumer(ConsoleCommandProcessor(comDict))


    def stopEverything() -> None:
        botRunning[0] = False


    comDict.bind(CommandSource.CONSOLE, "stop", (lambda args: stopEverything()))

    # Работа с браузером
    bc = BrowserController(proc)
    osite = OpenSite(proc)
    runjs = RunJavascript(proc)
    aler = AlertWaiter(proc)

    def saveDriverAndOpenPT(event: Event):
        driver: ChromiumDriver = event.args[0]

        openPonyTown = lambda: osite.start(driver, ["https://pony.town/"])
        executeAlert1 = lambda: runjs.start(driver, ["alert(1)"])
        waitForAlertClosing = lambda: aler.start(driver, [])
        setPonyTownCookies = lambda: runjs.start(driver, ["alert(2)"])
        clickPlay = lambda: runjs.start(driver, ["alert(3)"])

        doInChain(proc, [
            openPonyTown,
            executeAlert1,
            waitForAlertClosing,
            setPonyTownCookies,
            waitForAlertClosing,
            clickPlay
        ])

    doOnceEvent(proc, BrowserLoadedEvent.__name__,
                lambda event: saveDriverAndOpenPT(event))

    bc.start()

    # Цикл основного процесса
    try:
        while botRunning[0]:
            pass
    finally:
        ConsoleOutputter.toConsole("Finilizing!")
        aci.stop()
        proc.stop()
        bc.stop()
