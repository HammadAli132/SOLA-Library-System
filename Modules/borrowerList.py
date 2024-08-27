from Modules.borrower import Borrower

class BorrowerList:
    def __init__(self):
        self.__borrowersList = []

    @property
    def borrowersList(self): return self.__borrowersList

    def addNewBorrower(self, FN, LN, UN, Pass):
        borrower = Borrower(FN, LN, UN, Pass)
        self.__borrowersList.append(borrower)