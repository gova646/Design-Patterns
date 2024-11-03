
class Subject:
    observers = []

    def __init__(self, subjectName) -> None:
        self.subjectName = subjectName
        print(self.subjectName)

    def addObserver(self,observer):
        self.observers.append(observer)

    def removeObserver(self,observer):
        self.observers.remove(observer)
    
    def notifyAll(self,msg):
        for observer in self.observers:
            observer.update(msg)