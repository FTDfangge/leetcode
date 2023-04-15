# -*- coding: utf-8 -*-
# @Time    : 2022-03-16 10:31 p.m.
# @Author  : qkzhong
# @FileName: jianzhi22_getKth_from_end.py
# @Software: PyCharm

# AC

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        start = head
        end = start
        for i in range(k):
            end = end.next

        while end:
            start = start.next
            end = end.next

        return start
