from Modules.library import Library
from Modules.book import Book


def main():
    library = Library()
    book1 = Book(5, "Hobbit", "James Bond", "Adventures", "English", "2016", "Fiction")
    book2 = Book(3, "Rabbit", "James Bond", "Adventures", "English", "2016", "Fiction")
    book3 = Book(7, "Womit", "James Bond", "Adventures", "English", "2016", "Fiction")

    library.storage = book1
    library.storage = book2
    library.storage = book3

    library.display()
    

if __name__ == "__main__":
    main()