from factory import GUIFactory

class WindowsGUIFactory(GUIFactory):
    def getButton(self):
        print('Windows Button')
    
    def getCursor(self):
        print('Windows Cursor')