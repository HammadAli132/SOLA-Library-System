class TreeNode:
    def __init__(self, val):
        self.__data = val
        self.__left = None
        self.__right = None

    @property
    def data(self): return self.__data

    @data.setter
    def data(self, node): self.__data = node
    
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

    def _insert(self, root:TreeNode, val):
        if root is None:
            root = TreeNode(val)
            return root
        if root.data > val:
            root.left = self._insert(root.left, val)
        elif root.data <= val:
            root.right = self._insert(root.right, val)
        return root
    
    def _remove(self, root:TreeNode, val) -> TreeNode:
        if root is None:
            return root
        if val < root.data:
            root.left = self._remove(root.left, val)
        elif val > root.data:
            root.right = self._remove(root.right, val)
        else:
            if root.left is None: # Case 1
                return root.right
            elif root.right is None: # Case 2
                return root.left
            elif root.right is not None and root.left is not None: # Case 3
                inorderSuccessor:TreeNode = root.right
                while inorderSuccessor.left is not None:
                    inorderSuccessor = inorderSuccessor.left
                root.data = inorderSuccessor.data
                root.right = self._remove(root.right, inorderSuccessor.data)
            
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
    
    def add(self, val):
        self.__root = self._insert(self.__root, val)

    def delete(self, val):
        self.__root = self._remove(self.__root, val)

class ListNode:
    def __init__(self, val):
        self.__data = val
        self.__next = None
        self.__prev = None

    @property
    def data(self): return self.__data

    @data.setter
    def data(self, node): self.__data = node
    
    @property
    def next(self): return self.__next

    @next.setter
    def next(self, node): self.__next = node

    @property
    def prev(self): return self.__prev

    @prev.setter
    def prev(self, node): self.__prev = node

class DoublyLinkedList:
    def __init__(self):
        self.__head:ListNode = None

    @property
    def head(self): return self.__head

    def _insert(self, head:ListNode, val) -> ListNode:
        if head is None:
            head = ListNode(val)
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = ListNode(val)
            curr.next.prev = curr
        return head
    
    def _remove(self, head:ListNode, val) -> ListNode:
        if head.data == val:
            curr = head
            head = head.next
            head.prev = None
            curr.next = None
        else:
            curr = head
            while curr.next.data != val or curr.next is not None:
                curr.next = curr.next.next
                curr.next.prev = curr
        return head
    
    def search(self, head:ListNode, val) -> ListNode:
        curr = head
        while curr.data != val or curr is not None:
            curr = curr.next
        return curr.data
    
    def getItems(self, head:ListNode, list:list) -> None:
        curr = head
        while curr is not None:
            list.append(curr.data)
            curr = curr.next

    def add(self, val):
        self.__head = self._insert(self.__head, val)

    def delete(self, val):
        self.__head = self._remove(self.__head, val)