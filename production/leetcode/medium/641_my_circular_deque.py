# -*- coding: utf-8 -*-
# @Time    : 2022-08-15 11:01 a.m.
# @Author  : qkzhong
# @FileName: 641_my_circular_deque.py
# @Software: PyCharm


class MyCircularDeque:

    __slots__ = "max", "num", "deque"

    def __init__(self, k: int):
        self.max = k
        self.deque = []

    def insertFront(self, value: int) -> bool:
        return False


    def insertLast(self, value: int) -> bool:
        return False


    def deleteFront(self) -> bool:
        return False


    def deleteLast(self) -> bool:
        return False


    def getFront(self) -> int:
        return 0


    def getRear(self) -> int:
        return 0


    def isEmpty(self) -> bool:
        return False


    def isFull(self) -> bool:
        return False