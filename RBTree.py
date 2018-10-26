from enum import Enum


class Color(Enum):
    Red = 'Red'
    Black = 'Black'


class Node:

    def __init__(self, key, color=Color.Red, left=None, right=None, p=None):
        self.color = color
        self.key = key
        self.left = left if left else Nil
        self.right = right if right else Nil
        self.p = p


Nil = Node(None, color=Color.Black)


class RBTree:

    def __init__(self, ):
        pass


if __name__ == '__main__':
    print(12)
