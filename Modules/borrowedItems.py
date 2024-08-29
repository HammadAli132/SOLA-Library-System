from Modules.borrowedItem import BorrowedItem

class BorrowedItemsList:
    def __init__(self):
        self.__BIL = []

    @property
    def BIL(self): return self.__BIL

    def addNewBorrowedItem(self, borroweAN, itemName, itemID, date):
        borrowedItem = BorrowedItem(borroweAN, itemName, itemID, date)
        self.__BIL.append(borrowedItem)
    
    def deleteBorrowedItem(self, item):
        self.__BIL.remove(item)