class Item:
    currentId = 0
    def __init__(self, name, author, title, lang, yop, cat):
        Item.currentId += 1
        self.__itemId = Item.currentId
        self.__name = name
        self.__author = author
        self.__title = title
        self.__language = lang
        self.__yearOfPublication = yop
        self.__category = cat

    @property
    def itemId(self): return self.__itemId

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
