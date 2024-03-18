from event_engine.EventProcessor import EventProcessor
from event_engine.helpers.EventWatchers import doOnceEvent
from modules.browser.BrowserController import BrowserController
from modules.browser.events.BrowserLoadedEvent import BrowserLoadedEvent
from modules.browser.rountines.simple.OpenSite import OpenSite
from modules.comands.CommandDictionary import CommandDictionary
from modules.comands.CommandTypes import CommandSource
from modules.comands.console.ConsoleCommandProcessor import ConsoleCommandProcessor
from modules.console_io.ConsoleOutputter import ConsoleOutputter
from modules.console_io.events.ConsoleInputEvent import ConsoleInputEvent
from modules.console_io.producers.ConsoleInputer import AsyncConsoleInput

if __name__ == '__main__':
    proc = EventProcessor()
    proc.debugEventProcessing = True
    proc.debugEventConsuming = True
    proc.debugConsumersRemoving = True

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

    # Работа с браузером
    osite = OpenSite(proc)
    bc = BrowserController(proc)
    bc.start()
    doOnceEvent(proc, BrowserLoadedEvent.__name__,
                lambda event: osite.start(event.args[0], ["https://pony.town/"]))


    def stopEverything() -> None:
        botRunning[0] = False


    comDict.bind(CommandSource.CONSOLE, "stop", (lambda args: stopEverything()))

    try:
        while botRunning[0]:
            pass
    finally:
        ConsoleOutputter.toConsole("Finilizing!")
        aci.stop()
        proc.stop()
        bc.stop()
