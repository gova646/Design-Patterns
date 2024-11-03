from abc import abstractmethod,ABC

class Observer(ABC):
    @abstractmethod
    def update(self, msg):
        pass