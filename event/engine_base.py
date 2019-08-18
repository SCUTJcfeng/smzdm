
import traceback
from queue import Queue, Empty
from threading import Thread
from collections import defaultdict


class Event:
    def __init__(self, type_=None):
        self.type_ = type_
        self.dict_ = {}


class EventEngineBase(object):
    def __init__(self):
        self.__queue = Queue()
        self.__active = False
        self.__thread = Thread(target=self.__run)
        self.__handlers = defaultdict(list)
        self.__generalHandlers = []

    def __run(self):
        while self.__active is True:
            try:
                event = self.__queue.get(block=True, timeout=1)
                self.__process(event)
            except Empty:
                pass
            except:
                traceback.print_exc()

    def __process(self, event):
        if event.type_ in self.__handlers:
            [handler(event) for handler in self.__handlers[event.type_]]
        if self.__generalHandlers:
            [handler(event) for handler in self.__generalHandlers]

    def timerStart(self):
        raise NotImplementedError

    def timerStop(self):
        raise NotImplementedError

    def start(self, timer=True):
        self.__active = True
        self.__thread.start()
        if timer:
            self.timerStart()

    def stop(self):
        self.__active = False
        self.timerStop()
        self.__thread.join()

    def register(self, type_, handler):
        handlerList = self.__handlers[type_]
        if handler not in handlerList:
            handlerList.append(handler)

    def unregister(self, type_, handler):
        handlerList = self.__handlers[type_]
        if handler in handlerList:
            handlerList.remove(handler)
        if not handlerList:
            del self.__handlers[type_]

    def put(self, event):
        self.__queue.put(event)

    def registerGeneralHandler(self, handler):
        if handler not in self.__generalHandlers:
            self.__generalHandlers.append(handler)

    def unregisterGeneralHandler(self, handler):
        if handler in self.__generalHandlers:
            self.__generalHandlers.remove(handler)
