import abc

from ..event.event import Event

class Component:

    def __init__(self, event: Event):
        self._event = event

    @abc.abstractmethod
    def onStart(self):
        self._start_result = True

    @abc.abstractmethod
    def onExecute(self):
        self._execute_result = True

    @abc.abstractmethod
    def onEnd(self):
        self._end_result = True
