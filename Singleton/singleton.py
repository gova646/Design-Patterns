import threading

class Singleton:
    #Use a class variable to keep track of the instance created
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            #Make sure the creation of instance is thread safe.
            with cls._lock:
                if cls._instance is None:
                    print('Instance Created')
                    cls._instance = super(Singleton,cls).__new__(cls)
                return cls._instance
        print('Returning existing instance')
        return cls._instance
