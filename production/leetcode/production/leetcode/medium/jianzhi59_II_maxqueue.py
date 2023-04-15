# -*- coding: utf-8 -*-
# @Time    : 2022-04-02 4:51 p.m.
# @Author  : qkzhong
# @FileName: jianzhi59_II_maxqueue.py
# @Software: PyCharm
from collections import deque
from queue import Queue


class MaxQueue:
    __slots__ = 'max_queue', 'this_queue'
    def __init__(self):
        self.max_queue = deque()
        self.this_queue = Queue()

    def max_value(self) -> int:
        if self.max_queue:
            return self.max_queue[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.this_queue.put(value)
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()
        self.max_queue.append(value)

    def pop_front(self) -> int:
        if self.max_queue:
            res = self.this_queue.get()
            if res == self.max_queue[0]:
                self.max_queue.popleft()

            return res
        else:
            return -1
