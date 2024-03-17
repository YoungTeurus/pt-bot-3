from asyncio import get_event_loop

from console_io.consumers.PrintToConsoleConsumer import PrintToConsoleConsumer
from console_io.producers.AsyncConsoleInput import AsyncConsoleInput
from event_engine.EventProcessor import EventProcessor

loop = get_event_loop()

if __name__ == '__main__':
    proc = EventProcessor()

    proc.addConsumer(PrintToConsoleConsumer())
    aci = AsyncConsoleInput(proc)

    try:
        proc.run()

        aci.start(loop)
    except KeyboardInterrupt:
        print("Finishing!")
        aci.stop()
        proc.stop()
