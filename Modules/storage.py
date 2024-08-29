from Modules.item import Item
from Modules.dataStructures import BinarySearchTree

class Storage:
    def __init__(self):
        self.__store = BinarySearchTree()
        self.__totalItems = 0

    @property
    def store(self): return self.__store

    @store.setter
    def store(self, val):
        self.__store.add(val)
        self.__totalItems += 1

    def display(self):
        rack = []
        self.__store.getItems(self.__store.root, rack)
        for item in rack:
            print(item)

    def delete(self, val):
        self.__store.delete(val)
        self.__totalItems -= 1