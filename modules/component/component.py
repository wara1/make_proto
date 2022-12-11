import abc
from enum import Enum

class ComponentResult(Enum):
    BREAK = 0
    NEXT_EVENT = 1
    CONTINUE = 2

class Component:
    def __init__(self): {}

    @abc.abstractmethod
    def onStart(self) -> ComponentResult:
        self._start_result = True
        return ComponentResult.NEXT_EVENT

    @abc.abstractmethod
    def onExecute(self) -> ComponentResult:
        self._execute_result = True
        return ComponentResult.NEXT_EVENT

    @abc.abstractmethod
    def onEnd(self) -> ComponentResult:
        self._end_result = True
        return ComponentResult.NEXT_EVENT
