from abc import abstractmethod, ABC


class ModuleDefinition(ABC):
    @abstractmethod
    def requirements(self) -> None:
        raise NotImplemented

    @abstractmethod
    def init(self) -> None:
        raise NotImplemented
