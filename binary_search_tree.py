class BinarySearchTree:

    def __init__(self):
        self._tree = []

    def __getitem__(self, item):
        return Node(self, item)

    def __delitem__(self, key):
        return self._tree.__delitem__(key)

    def __len__(self):
        return self._tree.__len__()

    def __str__(self):
        return f'<BinarySearchTree {self._tree}>'

    def __repr__(self):
        return self.__str__()

    def insert(self, key):
        if len(self._tree) == 0:
            self._tree.append(key)
            return
        x = self[0]
        while True:
            if key < x.key and x.left:
                x = x.left
            elif key > x.key and x.right:
                x = x.right
            else:
                if key < x.key and not x.left:
                    index = x._left
                else:
                    index = x._right
                length = len(self)
                if index >= length:
                    self._tree.extend(None for _ in range(length, index + 1))
                self._tree[index] = key
                break


class Node:

    def __init__(self, tree: BinarySearchTree, index):
        self.tree = tree
        self.index = index
        self._right = (index << 1) + 2
        self._left = (index << 1) + 1

    @property
    def key(self):
        return self.tree._tree[self.index] if self.index < len(self.tree) else None

    @property
    def right(self):
        return Node(self.tree, self._right) if self._right < len(self.tree) else None

    @property
    def left(self):
        return Node(self.tree, self._left) if self._left < len(self.tree) else None

    def __bool__(self):
        return self.key is not None

    def __str__(self):
        return f'<BinarySearchTree.Node index: {self.index}, key: {self.key}>'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    a = BinarySearchTree()
    a.insert(200)
    a.insert(100)
    print(a)
