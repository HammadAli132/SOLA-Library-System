class BorrowedItem:
    def __init__(self, borroweAN, itemName, itemID, date):
        self.__borrowerAN = borroweAN
        self.__itemName = itemName
        self.__itemID = itemID
        self.__borrowDate = date

    @property
    def borrowerAN(self): return self.__borrowerAN

    @borrowerAN.setter
    def borrowerAN(self, val):
        self.__borrowerAN = val

    @property
    def itemName(self): return self.__itemName

    @itemName.setter
    def itemName(self, val):
        self.__itemName = val

    @property
    def itemID(self): return self.__itemID

    @itemID.setter
    def itemID(self, val):
        self.__itemID = val

    @property
    def borrowDate(self): return self.__borrowDate

    @borrowDate.setter
    def borrowDate(self, val):
        self.__borrowDate = val