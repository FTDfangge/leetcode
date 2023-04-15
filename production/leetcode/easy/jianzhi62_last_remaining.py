# -*- coding: utf-8 -*-
# @Time    : 2022-03-28 9:31 p.m.
# @Author  : qkzhong
# @FileName: jianzhi62_last_remaining.py
# @Software: PyCharm
from typing import List


class Linked_list:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.pre = None


def f(n, m):
    if n == 0:
        return 0
    x = f(n - 1, m)
    return (m + x) % n


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        head = Linked_list(0)
        ptr = head
        for i in range(1, n):
            ptr.next = Linked_list(i)
            ptr.next.pre = ptr
            ptr = ptr.next
        ptr.next = head
        head.pre = ptr

        while ptr.next.next != ptr.next:
            for step in range(m):
                ptr = ptr.next
            ptr.pre.next = ptr.next
            ptr.next.pre = ptr.pre
        return ptr.next.val

    def lastRemaining2(self, n: int, m: int) -> int:
        return f(n, m)


print(Solution().lastRemaining2(5, 3))
