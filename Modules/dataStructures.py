class TreeNode:
    def __init__(self, val):
        self.__data = val
        self.__left = None
        self.__right = None

    @property
    def data(self): return self.__data

    @property
    def left(self): return self.__left

    @left.setter
    def left(self, node): self.__left = node

    @property
    def right(self): return self.__right

    @right.setter
    def right(self, node): self.__right = node

class BinarySearchTree:
    def __init__(self):
        self.__root:TreeNode = None

    @property
    def root(self): return self.__root

    def insert(self, root:TreeNode, val):
        if root is None:
            root = TreeNode(val)
            return root
        if root.data > val:
            root.left = self.insert(root.left, val)
        elif root.data <= val:
            root.right = self.insert(root.right, val)
        return root
    
    def remove(self, root:TreeNode, val) -> TreeNode:
        if root is None:
            return root
        if val < root.data:
            root.left = self.remove(root.left, val)
        elif val >= root.data:
            root.right = self.remove(root.right, val)
        if root.left is None: # Case 1
            temp = root.right
            root = None
            return temp
        elif root.right is None: # Case 2
            temp = root.left
            root = None
            return temp
        elif root.right is not None and root.left is not None: # Case 3
            inorderSuccessor = root.right
            while inorderSuccessor.left is not None:
                inorderSuccessor = inorderSuccessor.left
            root.data = inorderSuccessor.data
            inorderSuccessor = None
            
        return root
    
    def search(self, root:TreeNode, val) -> TreeNode:
        if root is None:
            return root
        if root.data > val:
            return self.search(root.left, val)
        elif root.data <= val:
            return self.search(root.right, val)
        else:
            return root

    def getItems(self, root:TreeNode, list:list):
        if root is None:
            return
        if root.left:
            self.getItems(root.left, list)
        list.append(root.data)
        if root.right:
            self.getItems(root.right, list)
        return