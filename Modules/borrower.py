from __future__ import annotations
from Modules.user import User

class Borrower(User):
    def __init__(self, FN, LN, UN, Pass, AN):
        super().__init__(FN, LN, UN, Pass)
        self.__borrowerAN = AN
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

    def __str__(self) -> str:
        return f"""
    First Name: {super().firstName},
    Last Name: {super().lastName},
    Username: {super().username},
    Password: {super().password},
    Account Number: {self.__borrowerAN},
    Status: {super().status}
    """

    def __eq__(self, other:Borrower) -> bool:
        return self.__borrowerAN == other.borrowerAN

    def __ne__(self, other:Borrower) -> bool:
        return self.__borrowerAN != other.borrowerAN
    
    def borrowerManual() -> str:
        str = """
    1- Borrow an item from Library
    2- Return an item to Library
    3- Search for an item in Library
    4- Get details of an item
    5- Search all books by a specific author
    6- See borrow details"""
        return input(str)