from observer import Observer

class User(Observer):
    def __init__(self, name) -> None:
        self.name = name

    def update(self, msg):
        print(msg + ' recieved by ' + self.name)