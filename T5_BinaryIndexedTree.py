# Binary Indexed Tree / Fenwick Tree
# Date Created: 7 September 2018
# Created by Ravi garg


class FenwickTree:
    def __init__(self, arr):
        self.binaryIndexedTree = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            self.updateBinaryIndexedTree(arr[i - 1], i)

    def updateBinaryIndexedTree(self, val, index):
        while index < len(self.binaryIndexedTree):
            self.binaryIndexedTree[index] += val
            index = self.getNext(index)

    def getSum(self, index):
        index = index + 1
        sums = 0
        while index > 0:
            sums += self.binaryIndexedTree[index]
            index = self.getParent(index)
        return sums

    def getParent(self, index):
        return index - (index & (~(index) + 1))

    def getNext(self, index):
        return index + (index & (~(index) + 1))


if __name__ == "__main__":
    treeObj = FenwickTree([1, 2, 3, 4, -5, 6, 7])
    print(treeObj.getSum(0))
    print(treeObj.getSum(1))
    print(treeObj.getSum(2))
    print(treeObj.getSum(3))
    print(treeObj.getSum(4))
    print(treeObj.getSum(5))
    print(treeObj.getSum(6))
