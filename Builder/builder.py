#This is a Builder interface. Contains all the abstract methods 
# to be implemented by the concrete classes
from abc import abstractmethod,ABC
from desktop import Desktop

class DesktopBuilder(ABC):
    def __init__(self) -> None:
        self.desktop = Desktop()

    @abstractmethod
    def buildMouse(self):
        pass
    
    @abstractmethod
    def buildKeyboard(self):
        pass

    @abstractmethod
    def buildMonitor(self):
        pass
    
    def getDesktop(self):
        return self.desktop
