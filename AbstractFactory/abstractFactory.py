from macFactory import MacGUIFactory
from windowsFactory import WindowsGUIFactory
class AbstractFactory:
    
    def createFactory(self, osType):
        if osType == 'mac':
            return MacGUIFactory()
        elif osType == 'windows':
            return WindowsGUIFactory()
        else:
            raise Exception('Implementation of this factory is not possible')