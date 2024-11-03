from singleton import Singleton

instance1 = Singleton()
instance2 = Singleton()
print(instance1 is instance2)