from Modules.item import Item

class Storage:
    def __init__(self):
        self.__itemsList = []
        self.__totalItems = 0

    @property
    def itemsList(self): return self.__itemsList

    @itemsList.setter
    def itemsList(self, val):
        self.__itemsList.append(val)
        self.__totalItems += 1

    def __str__(self):
        return f"""
    {len(self.__itemsList)}"""