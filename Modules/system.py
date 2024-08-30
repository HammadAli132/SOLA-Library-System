import os
from Modules.storage import Storage
from Modules.admin import Admin
from Modules.borrowerList import BorrowerList
from Modules.borrowedItems import BorrowedItemsList

class System:
    def __init__(self):
        self.__admin = Admin("Hammad", "Ali", "admin", "admin")
        self.__storage = Storage()
        self.__borrowerList = BorrowerList()
        self.__borrowedItemsList = BorrowedItemsList()

    @property
    def admin(self): return self.__admin

    @property
    def storage(self): return self.__storage

    @property
    def borrowerList(self): return self.__borrowerList

    @property
    def borrowedItemsList(self): return self.__borrowedItemsList

    def adminSignIn(self):
        UN = input("Enter admin's username: ")
        Pass = input("Enter admin's password: ")
        return True if UN == self.__admin.username and Pass == self.__admin.password else False

    def operateAdmin(self):
        while (True):
            os.system("clear")
            option = self.__admin.adminManual()
            match option:
                case '1':
                    self.__admin.addNewItem(self.__storage)
                case '4':
                    self.__admin.displayStorage(self.__storage)
                case '5':
                    break

    def operateBorrower(self):
        ...