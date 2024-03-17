from event_engine.Event import Event, DEFAULT_PRIORITY


class SimpleMessageEvent(Event):
    def __init__(self, msg: str, priority: int = DEFAULT_PRIORITY):
        super().__init__(SimpleMessageEvent.__name__, [msg], priority)

    def _getArgsDescription(self) -> list[str]:
        return ["Message content"]
