from Modules.user import User

class Borrower(User):
    def __init__(self, FN, LN, UN, Pass):
        super().__init__(FN, LN, UN, Pass)
        self.__borrowerAN = ""
        self.__fine = 0

    @property
    def borrowerAN(self): return self.__borrowerAN

    @borrowerAN.setter
    def borrowerAN(self, val):
        self.__borrowerAN = val

    @property
    def fine(self): return self.__fine

    @fine.setter
    def fine(self, val):
        self.__fine += val