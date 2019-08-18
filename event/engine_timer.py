
from time import sleep
from threading import Thread
from .event_type import EVENT_TIMER
from .engine_base import EventEngineBase, Event


class EventEngineThreadTimer(EventEngineBase):
    def __init__(self, secods=1):
        EventEngineBase.__init__(self)
        self.__timer = Thread(target=self.__runTimer)
        self.__timerActive = False
        self.__timerSleep = secods

    def timerStart(self):
        self.__timerActive = True
        self.__timer.start()

    def timerStop(self):
        self.__timerActive = False
        self.__timer.join()

    def __runTimer(self):
        while self.__timerActive is True:
            event = Event(type_=EVENT_TIMER)
            self.put(event)
            sleep(self.__timerSleep)
