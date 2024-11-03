from factory import GUIFactory

class MacGUIFactory(GUIFactory):
    def getButton(self):
        print('Mac Button')
    
    def getCursor(self):
        print('Mac Cursor')