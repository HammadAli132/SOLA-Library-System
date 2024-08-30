import os
from Modules.user import User
from Modules.book import Book
from Modules.periodical import Periodical
from Modules.magazine import Magazine
from Modules.audioBook import AudioBook
from Modules.storage import Storage

class Admin(User):
    def __init__(self, FN, LN, UN, Pass):
        super().__init__(FN, LN, UN, Pass)

    def adminManual(self) -> str:
        str = """
    1- Add a new item to Library
    2- Search for an item in Library
    3- Get details of an item
    4- Get all items in library
    5- Exit
    Choice: """
        return input(str)
    
    def getNewBook(self) -> Book:
        os.system("clear")
        id = input("Enter the book's id: ")
        name = input("Enter the book's name: ")
        author = input("Enter the book's author: ")
        title = input("Enter the book's title: ")
        lang = input("Enter the book's language: ")
        YoP = input("Enter the year of publication: ")
        cat = input("Enter the category of the book: ")
        book = Book(id, name, author, title, lang, YoP, cat)
        chap = int(input("How many chapters does the book have: "))
        for i in range(chap):
            chapName = input(f"Enter Chapter {i + 1} title: ")
            book.chapters = {
                "chapter": i + 1,
                "name": chapName
            }
        quant = int(input("What's the quantity of this book: "))
        book.quantity = quant
        return book

    def addNewItem(self, storage:Storage):
        os.system("clear")
        option = input("What do you want to add?\n1- Book\n2- Magazine\n3- Periodical\n4- Audio Book\nChoice (1-4): ")
        match option:
            case '1':
                storage.store = self.getNewBook()
    
    def displayStorage(self, storage:Storage):
        os.system("clear")
        storage.display()