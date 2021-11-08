# -*- coding: utf-8 -*-
# @Time    : 2021-11-088:06 p.m.
# @Author  : raynor
# @FileName: 155_minStack.py
# @Software: PyCharm

#AC

class MinStack:
    __slots__ = {"stack"}

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            if val < self.stack[self.stack.__len__() - 1][1]:
                self.stack.append([val, val])
            else:
                self.stack.append([val, self.stack[self.stack.__len__() - 1][1]])


    def pop(self) -> None:
        self.stack.__delitem__(self.stack.__len__() - 1)

    def top(self) -> int:
        return self.stack[self.stack.__len__() - 1][0]

    def getMin(self) -> int:
        return self.stack[self.stack.__len__() - 1][1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(1)
    obj.push(1)
    obj.push(2)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
