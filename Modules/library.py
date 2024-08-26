from Modules.storage import Storage

class Library:
    def __init__(self):
        self.__store = Storage()

    @property
    def store(self): return self.__store

    @store.setter
    def store(self, item):
        self.__store.itemsList = item