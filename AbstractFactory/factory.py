from abc import abstractmethod,ABC

class GUIFactory(ABC):
    @abstractmethod
    def getButton(self):
        pass
    
    @abstractmethod
    def getCursor(self):
        pass
