# Max Heap
# Date Created: 27 August 2018
# Created by Ravi garg


from copy import deepcopy
class MaxHeap:
    def __init__(self, arr):
        self.heap = arr
        self.heapSize = len(self.heap)
        for i in range(self.heapSize//2, -1, -1):
            self.maxHeapify(i)

    def getHeapSize(self):
        return self.heapSize

    def getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1

    def getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2

    def getParentIndex(self, childIndex):
        return (childIndex - 1) // 2

    def hasLeftChild(self, parentIndex):
        return self.getLeftChildIndex(parentIndex) < self.heapSize

    def hasRightChild(self, parentIndex):
        return self.getRightChildIndex(parentIndex) < self.heapSize

    def hasParent(self, childIndex):
        return childIndex > 0

    def leftChild(self, index):
        return self.heap[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.heap[self.getRightChildIndex(index)]

    def parent(self, index):
        return self.heap[self.getParentIndex(index)]

    def heapifyUp(self, index):
        while self.hasParent(index) and self.parent(index) < self.heap[index]:
            self.heap[self.getParentIndex(index)], self.heap[
                index] = self.heap[index], self.heap[self.getParentIndex(
                    index)]
            index = self.getParentIndex(index)

    def heapifyDown(self, index):
        while self.hasLeftChild(index):
            biggerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(
                    index) > self.heap[biggerChildIndex]:
                biggerChildIndex = self.getRightChildIndex(index)
            if self.heap[biggerChildIndex] < self.heap[index]:
                self.heap[biggerChildIndex], self.heap[index] = self.heap[
                    index], self.heap[biggerChildIndex]
                index = biggerChildIndex
            else:
                break

    def getMaximum(self):
        if self.heapSize == 0:
            raise MemoryError("Heap is Empty")
        else:
            return self.heap[0]

    def extractMaximum(self):
        if self.heapSize == 0:
            raise MemoryError("Heap is Empty")
        else:
            item = self.heap[0]
            self.heap[0], self.heap[self.heapSize - 1] = self.heap[
                self.heapSize - 1], self.heap[0]
            self.heapSize -= 1
            self.heapifyDown(0)
            return item

    def addValue(self, value):
        self.heap[self.heapSize] = value
        self.heapSize += 1
        self.heapifyUp(self.heapSize - 1)

    def deleteKey(self, index):
        if index >= self.heapSize:
            raise IndexError("Index not found")
        self.heap[index] = 99999999999
        self.heapifyUp(index)
        self.extractMaximum()

    def deleteValue(self, value):
        if self.heapSize == 0:
            raise MemoryError("Heap is Empty")
        for index in range(self.heapSize):
            if self.heap[index] == value:
                self.deleteKey(index)
                return
        raise ValueError("Element not in Heap")

    def isEmpty(self):
        return self.heapSize == 0

    def maxHeapify(self, i, arr = None):
        if arr == None:
            arr = self.heap
        size = len(arr)
        if i >= size - 1:
            return arr
        else:
            left = i * 2 + 1
            right = i * 2 + 2
            maxi = i
            if left < size and arr[maxi] < arr[left]:
                maxi = left
            if right < size and arr[maxi] < arr[right]:
                maxi = right
            if maxi != i:
                arr[i], arr[maxi] = arr[maxi], arr[i]
                self.maxHeapify(maxi, arr)
            return arr

    def heapSort(self):
        arr = deepcopy(self.heap)
        n = len(arr)
        arr2 = []
        for i in range(n - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            arr2 += [arr.pop()]
            self.maxHeapify(0, arr)
        return arr2[::-1]

    def buildHeap(self, arr):
        n = len(arr)
        self.heap = arr
        self.heapSize = n
        for i in range(n//2, -1, -1):
            self.maxHeapify(i)

    def isMaxHeap(self, arr):
        return self.isMaxHeap2(arr, 0)

    def isMaxHeap2(self, arr, index):
        if index >= len(arr):
            return True
        leftIndex = index * 2 + 1
        rightIndex = index * 2 + 2
        if leftIndex >= len(arr):
            return True
        elif arr[leftIndex] > arr[index]:
            return False
        elif rightIndex < len(arr) and arr[rightIndex] > arr[index]:
            return False
        else:
            return self.isMaxHeap2(arr, leftIndex) and self.isMaxHeap2(
                arr, rightIndex)

    def getHeap(self):
        return self.heap

if __name__ == "__main__":
    obj = MaxHeap([2, 31, 20, 22, 10, 24, 1, 4])
    print(obj.heapSort())
    print(obj.getHeap())