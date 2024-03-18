from modules.ModuleDefinition import ModuleDefinition
from modules.console_io.ConsoleIO import ConsoleIO


class Commands(ModuleDefinition):
    def requirements(self) -> None:
        ConsoleIO()

    def init(self) -> None:
        pass
