class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.key}'

    def __str__(self):
        return self.__repr__()


class BinarySearchTree:
    root = None

    def __init__(self):
        self.root = None

    def insert(self, item: Node):
        if not self.root:
            self.root = item
        else:
            temp = self.root
            while temp:
                if item.key < temp.key:
                    if temp.left is not None:
                        temp = temp.left
                    else:
                        temp.left = item
                        break
                elif item.key > temp.key:
                    if temp.right is not None:
                        temp = temp.right
                    else:
                        temp.right = item
                        break
                else:
                    break

    def search(self, key):
        temp = self.root
        while temp:
            if temp.key < key:
                temp = temp.right
            elif temp.key > key:
                temp = temp.left
            else:
                return True
        else:
            return False

    def iter_self(self, item=None):
        if item is None:
            item = self.root
        if item.left is not None:
            self.iter_self(item.left)
        print(item.key)
        if item.right is not None:
            self.iter_self(item.right)
