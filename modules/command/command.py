from .. import component as cm

class Command:
    def __init__(self):
        self.__components = []

    def addComponent(self, component: cm.Component):
        self.__components.append(component)

    def execute(self):
        for component in self.__components:
            ret : cm.ComponentResult()
            events = [component.onStart, component.onExecute, component.onEnd]
            for event in events:
                ret = event()
                if cm.ComponentResult.NEXT_EVENT != ret:
                    # 次のイベントを実行しない
                    break
            if (cm.ComponentResult.BREAK == ret):
                # すべてのコマンド終了
                break
