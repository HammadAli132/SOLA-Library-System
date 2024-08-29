from __future__ import annotations
from typing import Any

class Item:
    currentId = 0
    def __init__(self,id,  name, author, title, lang, yop, cat):
        self.__itemId = id
        self.__name = name
        self.__author = author
        self.__title = title
        self.__language = lang
        self.__yearOfPublication = yop
        self.__category = cat

    @property
    def itemId(self): return self.__itemId

    @itemId.setter
    def itemId(self, val): self.__itemId = val

    @property
    def name(self): return self.__name

    @name.setter
    def name(self, val): self.__name = val

    @property
    def author(self): return self.__author

    @author.setter
    def author(self, val): self.__author = val

    @property
    def title(self): return self.__title

    @title.setter
    def title(self, val): self.__title = val

    @property
    def language(self): return self.__language

    @language.setter
    def language(self, val): self.__language = val

    @property
    def yearOfPublication(self): return self.__yearOfPublication

    @yearOfPublication.setter
    def yearOfPublication(self, val): self.__yearOfPublication = val

    @property
    def category(self): return self.__category

    @category.setter
    def category(self, val): self.__category = val

    def __eq__(self, other:Item) -> bool:
        return self.itemId == other.itemId
    
    def __gt__ (self, other:Item) -> bool:
        return self.itemId > other.itemId

    def __lt__ (self, other:Item) -> bool:
        return self.itemId < other.itemId

    def __le__ (self, other:Item) -> bool:
        return self.itemId <= other.itemId
