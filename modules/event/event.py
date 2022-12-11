from ..component.component import Component

class Event:
    def __init__(self):
        self.__components = []

    def addComponent(self, components: Component):
        self.__components = components

    def execute(self):
        for component in self.__components:
            component.onStart()
            component.onExecute()
            component.onEnd()
