# Binary Indexed Tree / Fenwick Tree
# Date Created: 7 September 2018
# Created by Ravi garg

# Note: The indexing done here is 1-based indexing


class FenwickTree:
    def __init__(self, arr):
        self.__inputArr = arr
        self.binaryIndexedTree = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            self.updateBinaryIndexedTree(arr[i - 1], i)

    def updateBinaryIndexedTree(self, val, index):
        while index < len(self.binaryIndexedTree):
            self.binaryIndexedTree[index] += val
            index = self.getNext(index)

    def updateOriginalArray(self, val, index):
        val = val - self.__inputArr[index - 1]
        self.__inputArr[index - 1] = val + self.__inputArr[index - 1]
        while index < len(self.binaryIndexedTree):
            self.binaryIndexedTree[index] += val
            index = self.getNext(index)

    def getSum(self, index):
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
    treeObj = FenwickTree([1, 2, 3, 4, 0, 6, 7])

    # Get sum of first 5 elements
    print(treeObj.getSum(5))

    # change value as 5 of original array at index 5
    treeObj.updateOriginalArray(val=5, index=5)
    print(treeObj.getSum(5))
