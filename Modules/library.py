from Modules.storage import Storage
from Modules.user import User
from Modules.borrowerList import BorrowerList
from Modules.borrowedItems import BorrowedItemsList

class Library:
    def __init__(self):
        self.__storage = Storage()
        self.__borrowerList = BorrowerList()

    @property
    def storage(self): return self.__storage

    @storage.setter
    def storage(self, item):
        self.__storage.store = item

    @property
    def borrowerList(self): return self.__borrowerList

    @borrowerList.setter
    def borrowerList(self, borrower):
        self.__borrowerList.addNewBorrower(borrower)

    def display(self):
        self.__borrowerList.display()

    def delete(self, val):
        self.__storage.delete(val)