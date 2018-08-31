# Disjoint Sets
# Date Created: 01 September 2018
# Created by Ravi garg


class DisjointSet:
    def __init__(self):
        self.map = dict()

    class Node:
        def __init__(self):
            self.data = 0
            self.parent = self
            self.rank = 0

    def makeSet(self, data):
        node = self.Node()
        node.data = data
        node.parent = node
        node.rank = 0
        self.map[data] = node

    def findSet(self, node):
        return self.__find(self.map[node]).data

    def __find(self, node):
        parent = node.parent
        if parent is node:
            return parent
        node.parent = self.__find(node.parent)
        return node.parent

    def union(self, data1, data2):
        node1 = self.map[data1]
        node2 = self.map[data2]
        parent1 = self.__find(node1)
        parent2 = self.__find(node2)
        if parent1.data == parent2.data:
            return False
        if parent1.rank >= parent2.rank:
            if parent1.rank == parent2.rank:
                parent1.rank = parent1.rank + 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2
        return True


if __name__ == "__main__":
    ds = DisjointSet()
    ds.makeSet(1)
    ds.makeSet(2)
    ds.makeSet(3)
    ds.makeSet(4)
    ds.makeSet(5)
    ds.makeSet(6)
    ds.makeSet(7)

    ds.union(1, 2)
    ds.union(2, 3)
    ds.union(4, 5)
    ds.union(6, 7)
    ds.union(5, 6)
    ds.union(3, 7)

    print(ds.findSet(1))
    print(ds.findSet(2))
    print(ds.findSet(3))
    print(ds.findSet(4))
    print(ds.findSet(5))
    print(ds.findSet(6))
    print(ds.findSet(7))
