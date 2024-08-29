from Modules.item import Item

class Periodical(Item):
    def __init__(self, id, name, author, title, lang, yop, cat):
        super().__init__(id, name, author, title, lang, yop, cat)
        self.__quantity = 0

    @property
    def quantity(self): return self.__quantity

    @quantity.setter
    def quantity(self, val): self.__quantity = val

    def __str__(self):
        return f"""
    Periodical Id: {super().itemId},
    Periodical Name: {super().name},
    Periodical Author: {super().author},
    Periodical Title: {super().title},
    Periodical Language: {super().language},
    Periodical Year of Publishment: {super().yearOfPublication},
    Periodical Category: {super().category},
    Periodical Quantity: {self.__quantity}"""