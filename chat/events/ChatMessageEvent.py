from event_engine.Event import Event


class ChatMessageEvent(Event):
    def _getArgsDescription(self) -> dict[str, object]:
        return {
            "Message author": str,
            "Message content": str,
            "Message flags": str
        }
