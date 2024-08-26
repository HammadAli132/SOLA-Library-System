from Modules.library import Library
from Modules.book import Book


def main():
    library = Library()
    book1 = Book("Hobbit", "James Bond", "Adventures", "English", "2016", "Fiction")

    library.store = book1
    print(book1)
    print(library.store)

if __name__ == "__main__":
    main()