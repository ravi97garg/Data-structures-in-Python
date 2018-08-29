# Merge Sort Tree
# Date Created: 29 August 2018
# Created by Ravi garg


from T2_SegmentTree import SegmentTree
class MergeSortTree(SegmentTree):
    def __init__(self, arr):
        SegmentTree.__init__(self, arr)

    def process(self, leftData, rightData):
        l = 0
        r = 0
        mergedList = []
        while l < len(leftData) and r < len(rightData):
            if leftData[l] < rightData[r]:
                mergedList.append(leftData[l])
                l += 1
            else:
                mergedList.append(rightData[r])
                r += 1
        while l < len(leftData):
            mergedList.append(leftData[l])
            l += 1
        while r < len(rightData):
            mergedList.append(rightData[r])
            r += 1
        return mergedList

    def leaf(self, index):
        return [self.arr[index]]

if __name__ == "__main__":
    obj = MergeSortTree([2, 4, 3, 6, 5, 8, 7])
    print(obj.getResult(2, 5))