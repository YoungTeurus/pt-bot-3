from event_engine.Event import Event, DEFAULT_PRIORITY


class ConsoleInputEvent(Event):
    def __init__(self, msg: str, priority: int = DEFAULT_PRIORITY):
        super().__init__([msg], priority)

    def _getArgsDescription(self) -> list[tuple[str, type]]:
        return [
            ("Message content", str)
        ]
