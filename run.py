
from handler import handler_keyword, handler_haojia
from event.engine_timer import EventEngineThreadTimer
from event.event_type import EVENT_TIMER


def timer_event_handler(event):
    handler_keyword()
    handler_haojia()


if __name__ == "__main__":
    engine = EventEngineThreadTimer(60)
    engine.register(EVENT_TIMER, timer_event_handler)
    engine.start()
    input()
