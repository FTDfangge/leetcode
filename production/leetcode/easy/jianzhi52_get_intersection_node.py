# -*- coding: utf-8 -*-
# @Time    : 2022-03-17 4:23 p.m.
# @Author  : qkzhong
# @FileName: jianzhi52_get_intersection_node.py
# @Software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptr_a = headA
        ptr_b = headB
        s = set()
        while ptr_a and ptr_b:
            if ptr_a == ptr_b:
                return ptr_a

            if ptr_a in s:
                return ptr_a
            elif ptr_b in s:
                return ptr_b
            else:
                s.add(ptr_a)
                s.add(ptr_b)
            ptr_a = ptr_a.next
            ptr_b = ptr_b.next

        while ptr_a:
            if ptr_a in s:
                return ptr_a
            else:
                s.add(ptr_a)
            ptr_a = ptr_a.next

        while ptr_b:
            if ptr_b in s:
                return ptr_b
            else:
                s.add(ptr_b)
            ptr_b = ptr_b.next

        return None