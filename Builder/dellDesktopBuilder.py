from builder import DesktopBuilder
from desktop import Desktop

class DellDesktopBuilder(DesktopBuilder): 
    def buildMouse(self):
        self.desktop.setMouse('Dell Mouse')
    
    def buildKeyboard(self):
        self.desktop.setKeyboard('Dell Keyboard')

    def buildMonitor(self):
        self.desktop.setMonitor('Dell Monitor')
    
    def getDesktop(self):
        return self.desktop