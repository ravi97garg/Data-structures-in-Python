# Binary Search Tree
# Date Created: 22 August 2018
# Created by Ravi garg


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        root = self.root
        if root is None:
            self.root = Node(data)
        else:
            while True:
                if root.left is None and root.data > data:
                    root.left = Node(data)
                    break
                elif root.right is None and root.data <= data:
                    root.right = Node(data)
                    break
                else:
                    if root.data > data:
                        root = root.left
                    else:
                        root = root.right

    def minVal(self):
        root = self.root
        while root.left is not None:
            root = root.left
        return root.data

    def maxVal(self):
        root = self.root
        while root.right is not None:
            root = root.right
        return root.data


def printBST(root):
    if root:
        printBST(root.left)
        print(root.data, end=" ")
        printBST(root.right)


if __name__ == "__main__":
    tree = BSTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(4)
    print(tree.minVal())
    print(tree.maxVal())
    printBST(tree.root)

