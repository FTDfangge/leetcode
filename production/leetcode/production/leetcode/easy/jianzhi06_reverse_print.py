# -*- coding: utf-8 -*-
# @Time    : 2022-03-11 3:16 p.m.
# @Author  : qkzhong
# @FileName: jianzhi06_reverse_print.py
# @Software: PyCharm

#AC
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.output = []

    def reversePrint(self, head: ListNode) -> List[int]:
        if head != None:
            if head.next != None:
                self.reversePrint(head.next)
            self.output.append(head.val)
        return self.output
