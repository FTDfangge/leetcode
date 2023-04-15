# -*- coding: utf-8 -*-
# @Time    : 2022-03-19 9:50 p.m.
# @Author  : qkzhong
# @FileName: jianzhi41_median_finder.py
# @Software: PyCharm

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []


    def addNum(self, num: int) -> None:
        self.list.append(num)
        self.list.sort()


    def findMedian(self) -> float:
        length = self.list.__len__()
        if length % 2 != 0:
            return self.list[(length - 1)//2]
        else:
            return (self.list[length // 2] + self.list[(length - 1) // 2]) / 2