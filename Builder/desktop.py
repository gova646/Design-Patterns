#This is the Product Class
class Desktop:
    mouse = None
    keyboard = None
    monitor = None

    def __init__(self) -> None:
        pass
    
    def setMouse(self, mouse):
        self.mouse = mouse
    
    def setKeyboard(self, keyboard):
        self.keyboard = keyboard
        
    def setMonitor(self, monitor):
        self.monitor = monitor

    def showSpecs(self):
        print(self.mouse)
        print(self.keyboard)
        print(self.monitor)
