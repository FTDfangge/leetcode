# -*- coding: utf-8 -*-
# @Time    : 2022-03-11 2:44 p.m.
# @Author  : qkzhong
# @FileName: jianzhi09_stack_to_queue.py
# @Software: PyCharm

#AC

class CQueue:
    __slots__ = "stack1", "stack2"
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2.__len__() > 0:
            return self.stack2.pop()
        else:
            if self.stack1.__len__() > 0:
                while self.stack1.__len__() > 0:
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
            else:
                return -1