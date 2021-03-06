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

    def maxVal(self):
        root = self.root
        while root.right is not None:
            root = root.right
        return root.data

    def minVal(self):
        root = self.root
        while root.left is not None:
            root = root.left
        return root.data

    def search(self, key):
        root = self.root
        while root is not None:
            if key == root.data:
                return 1
            elif key > root.data:
                root = root.right
            else:
                root = root.left
        return 0

    def remove(self, key):
        remove(self.root, key)

    def longestPathlength(self, root = None):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        else:
            count = 1 + max(self.longestPathlength(root.left), self.longestPathlength(root.right))
        return count

    def getRoot(self):
        return self.root

    def levelOrder(self):
        queue = [self.root]
        self.__level(queue)

    def __level(self, queue):
        while len(queue):
            current = queue[0]
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            queue = queue[1:]
            print(current.data, sep=' ', end=' ')

def printBST(root):
    if root:
        printBST(root.left)
        print(root.data, end=" ")
        printBST(root.right)

def remove(root, key):
    if root is None:
        return None
    elif root.data > key:
        root.left = remove(root.left, key)
    elif root.data < key:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            root2 = root.left
            while root2.right is not None:
                root2 = root2.right
            root.left = root2
            root.data = root2.data
            root.right = remove(root.right, root2.key)
    return root


if __name__ == "__main__":
    tree = BSTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(4)
    tree.insert(2)
    print('Height of the tree is', tree.longestPathlength(tree.getRoot()))
    tree.levelOrder()
    print()
    printBST(tree.root)

