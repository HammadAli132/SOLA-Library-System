from Modules.item import Item

class Magazine(Item):
    def __init__(self, name, author, title, lang, yop, cat):
        super().__init__(name, author, title, lang, yop, cat)
        self.__quantity = 0

    @property
    def quantity(self): return self.__quantity

    @quantity.setter
    def quantity(self, val): self.__quantity = val

    def __str__(self):
        return f"""
    Magazine Id: {super().itemId},
    Magazine Name: {super().name},
    Magazine Author: {super().author},
    Magazine Title: {super().title},
    Magazine Language: {super().language},
    Magazine Year of Publishment: {super().yearOfPublication},
    Magazine Category: {super().category},
    Magazine Quantity: {self.__quantity}"""