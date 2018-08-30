# DoublyLinkedList
# Date Created: 30 July 2018
# Created by Ravi garg


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

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

    def setPrev(self, prev):
        self.prev = prev

    def getPrev(self):
        return self.prev

    def hasPrev(self):
        return self.prev is not None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data, None, current)
            self.tail = current.next

    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            self.head.prev = None
            return True

        if current is None:
            return False

        if self.tail == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return True

        while current is not None:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
            current = current.next

        return False

    def insertAtBeginning(self, data):
        newNode = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.setPrev(None)
            newNode.set_next(self.head)
            self.head.setPrev(newNode)
            self.head = newNode

    def getNode(self, index):
        currentNode = self.head
        if currentNode is None:
            return None
        i = 0
        while i < index and currentNode.get_next() is not None:
            currentNode = currentNode.get_next()
            if currentNode is None:
                break
            i += 1
        return currentNode

    def insertAtGivenPosition(self, index, data):
        newNode = Node(data)
        if self.head is None or index == 0:
            self.insertAtBeginning(data)
        elif index > 0:
            temp = self.getNode(index)
            if temp is None or temp.get_next() is None:
                self.insert(data)
            else:
                newNode.set_next(temp.get_next())
                newNode.setPrev(temp)
                temp.get_next().setPrev(newNode)
                temp.set_next(newNode)

    def find(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def fwd_print(self):
        current = self.head
        if current is None:
            print("No elements")
            return False
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        return True

    def rev_print(self):
        current = self.tail
        if self.tail is None:
            print("No elements")
            return False

        while current is not None:
            print(current.data, end=' ')
            current = current.prev
        return True


if __name__ == '__main__':
    l = DoublyLinkedList()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)

    l.fwd_print()
    l.rev_print()
    if l.find(3):
        print("Found")
    else:
        print("Not found")
    l.delete(3)
    if l.find(3):
        print("Found")
    else:
        print("Not found")
