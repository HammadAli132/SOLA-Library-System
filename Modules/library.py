from Modules.storage import Storage
from Modules.user import User
from Modules.borrowerList import BorrowerList
from Modules.borrowedItems import BorrowedItemsList

class Library:
    def __init__(self):
        self.__storage = Storage()

    @property
    def storage(self): return self.__storage

    @storage.setter
    def storage(self, item):
        self.__storage.store = item

    def display(self):
        self.__storage.display()