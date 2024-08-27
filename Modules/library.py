from Modules.storage import Storage
from Modules.user import User
from Modules.borrowerList import BorrowerList
from Modules.borrowedItems import BorrowedItemsList

class Library:
    def __init__(self):
        self.__store = Storage()

    @property
    def store(self): return self.__store

    @store.setter
    def store(self, item):
        self.__store.itemsList = item