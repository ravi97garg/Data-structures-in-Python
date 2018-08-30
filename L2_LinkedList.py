# Linked List
# Date Created: 28 July 2018
# Created by Ravi garg


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None


class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def addNode(self, node):
        if self.length == 0:
            self.addBeg(node)
        else:
            self.addLast(node)

    def addBeg(self, node):
        newNode = node
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def addAfterValue(self, data, node):
        newNode = node
        currentnode = self.head

        while currentnode.next is not None or currentnode.data != data:
            if currentnode.data == data:
                newNode.next = currentnode.next
                currentnode.next = newNode
                self.length = self.length + 1
                return
            else:
                currentnode = currentnode.next

        print("The data provided is not present")

    def addAtPos(self, pos, node):
        count = 0
        currentnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while currentnode.next is not None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = node
                    node.next = currentnode
                    self.length += 1
                    return

                else:
                    previousnode = currentnode
                    currentnode = currentnode.next

    def addLast(self, node):
        currentnode = self.head

        while currentnode.next is not None:
            currentnode = currentnode.next

        newNode = node
        newNode.next = None
        currentnode.next = newNode
        self.length = self.length + 1

    def deleteBeg(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            self.length -= 1

    def deleteLast(self):

        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head

            while currentnode.next is not None:
                previousnode = currentnode
                currentnode = currentnode.next

            previousnode.next = None

            self.length -= 1

    # method to delete a node after the node having the given data
    def deleteValue(self, data):
        currentnode = self.head
        previousnode = self.head

        while currentnode.next is not None or currentnode.data != data:
            if currentnode.data == data:
                previousnode.next = currentnode.next
                self.length -= 1
                return

            else:
                previousnode = currentnode
                currentnode = currentnode.next

        print("The data provided is not present")

    def deleteAtPos(self, pos):
        count = 0
        currentnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        elif pos == 1:
            self.delete_beg()
            self.length -= 1
        else:
            while currentnode.next is not None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next

    def getLength(self):
        return self.length

    def getFirst(self):
        if self.length == 0:
            print("The list is empty")
        else:
            return self.head.data

    def getLast(self):

        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head

            while currentnode.next is not None:
                currentnode = currentnode.next

            return currentnode.data

    def getAtPos(self, pos):
        count = 0
        currentnode = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while currentnode.next is not None or count < pos:
                count = count + 1
                if count == pos:
                    return currentnode.data
                else:
                    currentnode = currentnode.next

    def print_list(self):
        nodeList = []
        currentnode = self.head
        while currentnode is not None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.next

        print(nodeList)


class BSTNode:
    def __init__(root, data=None):
        root.left = None
        root.right = None
        root.data = data


def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insertNode(root.right, node)


def deleteNode(root, data):
    if root.data == data:
        if root.right and root.left:
            [psucc, succ] = findMin(root.right, root)
            if psucc.left == succ:
                psucc.left = succ.right
            else:
                psucc.right = succ.right
            succ.left = root.left
            succ.right = root.right
            return succ
        else:
            if root.left:
                return root.left
            else:
                return root.right
    else:
        if root.data > data:
            if root.left:
                root.left = deleteNode(root.left, data)
        else:
            if root.right:
                root.right = deleteNode(root.right, data)
    return root


def findMin(root, parent):
    if root.left:
        return findMin(root.left, root)
    else:
        return [parent, root]


def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data)
    inOrderTraversal(root.right)


def preOrderTraversal(root):
    if not root:
        return
    print(root.data)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    ll = LinkedList()
    ll.addNode(node1)
    ll.addNode(node2)
    ll.addNode(node3)
    ll.addNode(node4)
    ll.addNode(node5)
    ll.print_list()
