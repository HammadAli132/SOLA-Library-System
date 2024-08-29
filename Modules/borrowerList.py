from Modules.borrower import Borrower
from Modules.dataStructures import DoublyLinkedList

class BorrowerList:
    def __init__(self):
        self.__borrowersList = DoublyLinkedList()

    @property
    def borrowersList(self): return self.__borrowersList

    def addNewBorrower(self, borrower):
        self.__borrowersList.add(borrower)

    def remove(self, borrower):
        self.__borrowersList.delete(borrower)

    def display(self):
        list = []
        self.__borrowersList.getItems(self.__borrowersList.head, list)
        for borrower in list:
            print(borrower)