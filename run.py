
from handler import handler_keyword
from event.engine_timer import EventEngineThreadTimer
from event.event_type import EVENT_TIMER


def general_event_handler(event):
    if event.type_ == EVENT_TIMER:
        handler_keyword()


if __name__ == "__main__":
    engine = EventEngineThreadTimer(60)
    engine.registerGeneralHandler(general_event_handler)
    engine.start()
    input()
