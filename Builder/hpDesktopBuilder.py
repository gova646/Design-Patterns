from builder import DesktopBuilder

class HpDesktopBuilder(DesktopBuilder):
    def buildMouse(self):
        self.desktop.setMouse('HP Mouse')
    
    def buildKeyboard(self):
        self.desktop.setKeyboard('HP Keyboard')

    def buildMonitor(self):
        self.desktop.setMonitor('HP Monitor')

    def getDesktop(self):
        return self.desktop