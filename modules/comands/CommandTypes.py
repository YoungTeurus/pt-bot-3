from enum import Enum
from typing import Callable


class CommandSource(Enum):
    CONSOLE = 1
    CHAT = 2


ACTION = Callable[[list], None]
UNBIND_ACTION = Callable[[], None]
