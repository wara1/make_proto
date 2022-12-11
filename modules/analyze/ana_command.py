import sys

from .. import command as cmd
from .. import component as cm

class AnaCommand:

    def __init__(self, args):
        self.__command :cmd.Command= cmd.Command()

        self.__command.addComponent(cm.AutoGenerate())
        self.__command.addComponent(cm.CharCodeConvert())
        self.__command.addComponent(cm.DlPloto())
        self.__command.addComponent(cm.Help())

    def getCommand(self):
        return self.__command