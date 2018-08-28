# Segment Tree / Statistic Tree
# Date Created: 28 August 2018
# Created by Ravi garg


from math import log, ceil
from abc import ABC, abstractmethod


class SegmentTree(ABC):
    def __init__(self, arr):
        self.arr = arr
        self.size = 2 ** (ceil(log(len(self.arr), 2)) + 1) - 1
        self.tree = [None] * self.size
        self.buildSegmentTree()

    @abstractmethod
    def process(self, leftData, rightData):
        pass

    @abstractmethod
    def leaf(self, index):
        pass

    def buildSegmentTree(self, start=None, end=None, index=0):
        if start is None:
            start = 0
        if end is None:
            end = len(self.arr) - 1
        if start > end or index >= self.size:
            return
        elif start == end:
            self.tree[index] = self.leaf(start)  # self.arr[start]
        else:
            mid = (start + end) // 2
            self.buildSegmentTree(start, mid, index * 2 + 1)
            self.buildSegmentTree(mid + 1, end, index * 2 + 2)
            self.tree[index] = self.process(self.tree[index * 2 + 1], self.tree[index * 2 + 2])

    def overlap(self, start, end, queryStart, queryEnd):
        mid = (start + end) // 2
        if queryStart <= start and end <= queryEnd:
            return 1
        elif mid >= queryEnd:
            return 2
        elif mid < queryStart:
            return 3
        return 4

    def getResult(self, queryStart, queryEnd, start=None, end=None, index=0):
        if start is None:
            start = 0
        if end is None:
            end = len(self.arr) - 1
        overlapValue = self.overlap(start, end, queryStart, queryEnd)
        mid = (start + end) // 2
        if overlapValue == 1:
            return self.tree[index]
        elif overlapValue == 2:
            return self.getResult(queryStart, queryEnd, start, mid, 2 * index + 1)
        elif overlapValue == 3:
            return self.getResult(queryStart, queryEnd, mid + 1, end, 2 * index + 2)
        elif overlapValue == 4:
            left = self.getResult(queryStart, queryEnd, start, mid, 2 * index + 1)
            right = self.getResult(queryStart, queryEnd, mid + 1, end, 2 * index + 2)
            return self.process(left, right)
        return None
