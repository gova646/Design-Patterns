# Director Makes the call to build processes.

class DesktopDirector:
    def __init__(self, desktopBuilder) -> None:
        self.desktopBuilder = desktopBuilder

    def buildDesktop(self):
        self.desktopBuilder.buildMouse()
        self.desktopBuilder.buildKeyboard()
        self.desktopBuilder.buildMonitor()
        return self.desktopBuilder.getDesktop()

    def getDesktop(self):
        return self.desktopBuilder.getDesktop()