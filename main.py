from Modules.library import Library
from Modules.book import Book
from Modules.borrower import Borrower


def main():
    library = Library()
    book1 = Book(5, "Hobbit", "James Bond", "Adventures", "English", "2016", "Fiction")
    book2 = Book(3, "Rabbit", "James Bond", "Adventures", "English", "2016", "Fiction")
    book3 = Book(7, "Womit", "James Bond", "Adventures", "English", "2016", "Fiction")
    book7 = Book(8, "Womit", "James Bond", "Adventures", "English", "2016", "Fiction")

    b1 = Borrower("Hammad", "Ali", "@hammadali", "123", "5235")
    b2 = Borrower("Hashir", "Ali", "@hashirali", "123", "5200")
    b3 = Borrower("Hashir", "Faizan", "@hashirali", "123", "3200")

    library.storage = book1
    library.storage = book2
    library.storage = book3

    library.borrowerList = b1
    library.borrowerList = b2
    library.borrowerList = b3

    library.display()
    library.delete(b1)
    library.display()

    # library.delete(book7)

    # library.display()

if __name__ == "__main__":
    main()