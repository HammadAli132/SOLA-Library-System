from Modules.item import Item

class AudioBook(Item):
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
        str = ""
        for chap in self.__chapters:
            str += f"\n{chap['chapter']} has Duration {chap['time']}"
        return str

    def __str__(self):
        return f"""
    Audio Book Id: {super().itemId},
    Audio Book Name: {super().name},
    Audio Book Author: {super().author},
    Audio Book Title: {super().title},
    Audio Book Language: {super().language},
    Audio Book Chapters: {self.getChapters()},
    Audio Book Year of Publishment: {super().yearOfPublication},
    Audio Book Category: {super().category},
    Audio Book Quantity: {self.__quantity}"""