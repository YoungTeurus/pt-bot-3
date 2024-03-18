from event_engine.Event import Event, DEFAULT_PRIORITY


class RoutineStartEvent(Event):

    def __init__(self, args: list[object], priority: int = DEFAULT_PRIORITY):
        super().__init__(args, priority)

    def _getArgsDescription(self) -> list[tuple[str, type]]:
        return [
            ("Routine name", str),
            ("Routine args", list)
        ]