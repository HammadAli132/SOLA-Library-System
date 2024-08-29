from typing import Any
from Modules.item import Item

class Book(Item):
    def __init__(self, id, name, author, title, lang, yop, cat):
        super().__init__(id, name, author, title, lang, yop, cat)
        self.__quantity = 0
        self.__chapters = []

    @property
    def quantity(self): return self.__quantity

    @quantity.setter
    def quantity(self, val): self.__quantity = val

    @property
    def chapters(self): return self.__chapters

    @chapters.setter
    def chapters(self, val): self.__chapters = val

    def getChapters(self):
        if len(self.__chapters) == 0:
            return "None"
        str = ""
        for chap in self.__chapters:
            str += f"\n{chap['chapter']} on Page {chap['page']}"
        return str

    def __str__(self):
        return f"""
    Book Id: {super().itemId},
    Book Name: {super().name},
    Book Author: {super().author},
    Book Title: {super().title},
    Book Language: {super().language},
    Book Chapters: {self.getChapters()},
    Book Year of Publishment: {super().yearOfPublication},
    Book Category: {super().category},
    Book Quantity: {self.__quantity}"""