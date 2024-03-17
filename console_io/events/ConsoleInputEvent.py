from event_engine.Event import Event, DEFAULT_PRIORITY


class ConsoleInputEvent(Event):
    def __init__(self, msg: str, priority: int = DEFAULT_PRIORITY):
        super().__init__(ConsoleInputEvent.__name__, [msg], priority)

    def _getArgsDescription(self) -> dict[str, object]:
        return {
            "Message content": str
        }
