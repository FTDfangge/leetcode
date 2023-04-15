# -*- coding: utf-8 -*-
# @Time    : 2022-03-16 9:44 p.m.
# @Author  : qkzhong
# @FileName: jianzhi18_delete_node.py
# @Software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # AC, and already better than most of the solution on website, but not good enough
        if head.val == val:
            head = head.next

        ptr = head

        while ptr:
            if ptr.next:
                if ptr.next.val == val:
                    ptr.next = ptr.next.next
            ptr = ptr.next
        return head


if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    print(Solution().deleteNode(head, 5))
