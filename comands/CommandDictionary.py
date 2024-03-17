from comands.CommandTypes import ACTION, UNBIND_ACTION, CommandSource


class CommandDictionary:
    __commands: dict[CommandSource, dict[str, ACTION]]

    def __init__(self):
        self.__commands = {source: {} for source in CommandSource}

    def bind(self, source: CommandSource, command: str, action: ACTION) -> UNBIND_ACTION:
        if command in self.__commands[source]:
            raise KeyError(f"Command {command} for {source.name} already binded")
        self.__commands[source][command] = action
        return lambda: self.unbind(source, command)

    def unbind(self, source: CommandSource, command: str) -> None:
        if command not in self.__commands[source]:
            raise KeyError(f"Command {command} for {source.name} is not binded")
        self.__commands[source].pop(command)

    def findAction(self, source: CommandSource, command: str) -> ACTION | None:
        if command in self.__commands[source]:
            return self.__commands[source][command]
        return None
