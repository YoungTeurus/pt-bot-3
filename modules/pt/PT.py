from modules.ModuleDefinition import ModuleDefinition
from modules.browser.Browser import BrowserModule


class PTModule(ModuleDefinition):
    def requirements(self) -> None:
        BrowserModule()

    def init(self) -> None:
        pass