import sys

from .. import command as cmd
from .. import component as cm

class AnaCommand:

    def __init__(self, args):
        self.__command :cmd.Command= cmd.Command()
        self.__command.addComponent(cm.Component())

    def getCommand(self):
        return self.__command