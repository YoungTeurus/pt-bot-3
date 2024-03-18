from event_engine.Event import Event, DEFAULT_PRIORITY, EVENT_ARGS_DESCRIPTION


class ConsoleInputEvent(Event):
    def __init__(self, msg: str, priority: int = DEFAULT_PRIORITY):
        super().__init__([msg], priority)

    def _getArgsDescription(self) -> EVENT_ARGS_DESCRIPTION:
        return [
            ("Message content", str)
        ]
