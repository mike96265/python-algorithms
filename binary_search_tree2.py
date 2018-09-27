class BinarySearchTree:

    def __init__(self):
        self.start = None

    def insert(self, key):
        if not self.start:
            self.start = Node(key)
        else:
            x = self.start
            while True:
                if key < x.key and x.left is not None:
                    x = x.left
                elif key > x.right and x.right is not None:
                    x = x.right
                else:
                    if key < x.key and x.left is None:
                        x.left = Node(key)
                    else:
                        x.right = Node(key)

    def search(self, k):
        x = self.start
        while x:
            if k < x.key and x.left:
                x = x.left
            elif k > x.key and x.right:
                x = x.right
            elif k == x.key:
                return True
            else:
                return None

    def __str__(self):
        return '<BinarySearchTree {}>'.format(self.__hash__())

    def __repr__(self):
        return self.__str__()

    def walk(self, x=None, f=1):
        if f == 1:
            x = self.start
        if x is not None:
            self.walk(x.left, 0)
            print(x.key)
            self.walk(x.right, 0)


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return f'<BinarySearchTree.Node key:{self.key}>'

    def __repr__(self):
        return self.__str__()
