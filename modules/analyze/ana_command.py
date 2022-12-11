import sys

from ..event.event import Event
from ..component.component import Component

class AnaCommand:
    def __init__(self, args):
        self.__event = Event()
        self.__event.addComponent(Component(self.__event))

    def getEvent(self):
        return self.__event