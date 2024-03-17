from comands.CommandDictionary import CommandDictionary
from comands.CommandTypes import CommandSource
from comands.console.ConsoleCommandProcessor import ConsoleCommandProcessor
from console_io.ConsoleOutputter import ConsoleOutputter
from console_io.producers.ConsoleInputer import AsyncConsoleInput
from event_engine.EventProcessor import EventProcessor

if __name__ == '__main__':
    proc = EventProcessor(debugAllEvents=True)
    proc.start()

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

    try:
        while botRunning[0]:
            pass
    finally:
        ConsoleOutputter.toConsole("Finilizing!")
        aci.stop()
        proc.stop()
