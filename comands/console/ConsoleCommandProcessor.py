from comands.CommandConfig import COMMAND_PREFIX, COMMAND_PREFIX_LENGTH
from comands.CommandDictionary import CommandDictionary
from comands.CommandTypes import CommandSource
from console_io.ConsoleOutputter import ConsoleOutputter
from console_io.events.ConsoleInputEvent import ConsoleInputEvent
from event_engine.Event import Event
from event_engine.EventConsumer import EventConsumer
from shlex import split


class ConsoleCommandProcessor(EventConsumer):
    __comDict: CommandDictionary

    def __init__(self, comDict: CommandDictionary):
        super().__init__([ConsoleInputEvent.__name__])
        self.__comDict = comDict

    def _doConsume(self, event: Event) -> Event | None:
        inputContent: str = event.args[0]

        if inputContent.startswith(COMMAND_PREFIX):
            commandAndArgs = split(inputContent[COMMAND_PREFIX_LENGTH:])
            command = commandAndArgs[0]
            maybeAction = self.__comDict.findAction(CommandSource.CONSOLE, command)
            if maybeAction is None:
                ConsoleOutputter.toConsole(f"Console command {command} was not found")
            else:
                maybeAction(commandAndArgs[1:])

        return event
