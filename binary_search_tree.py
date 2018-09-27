class BinarySearchTree:

    def __init__(self):
        self._tree = []

    def __getitem__(self, item):
        return Node(self, item)

    def __setitem__(self, key, value):
        return self._tree.__setitem__(key , value)

    def __delitem__(self, key):
        return self._tree.__delitem__(key)

    def __len__(self):
        return self._tree.__len__()

    def __str__(self):
        return f'<BinarySearchTree {self._tree}>'

    def __repr__(self):
        return self.__str__()

    def getvalue(self, item):
        return self._tree[item - 1]


class Node:

    def __init__(self, tree: BinarySearchTree, index):
        self.tree = tree
        self.index = index
        self._right = (index << 1) + 2
        self._left = (index << 1) + 1

    @property
    def key(self):
        return self.tree._tree[self.index] if self.index <= len(self.tree) else None

    @property
    def right(self):
        return Node(self.tree, self._right) if self._right <= len(self.tree) else None

    @property
    def left(self):
        return Node(self.tree, self._left) if self._left <= len(self.tree) else None

    def __str__(self):
        return f'<BinarySearchTree.Node index: {self.index}, key: {self.key}>'

    def __repr__(self):
        return self.__str__()
