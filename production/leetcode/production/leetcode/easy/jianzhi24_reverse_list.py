# -*- coding: utf-8 -*-
# @Time    : 2022-03-11 3:30 p.m.
# @Author  : qkzhong
# @FileName: jianzhi24_reverse_list.py
# @Software: PyCharm

#AC

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            ptr = head
            left = ptr
            ptr = ptr.next
            while ptr is not None:
                right = ptr.next
                ptr.next = left
                left = ptr
                ptr = right
            head.next = None
        else:
            left = None
        return left


if __name__ == '__main__':
    head = ListNode(1)
    ptr = head
    ptr.next = ListNode(2)
    ptr = ptr.next
    ptr.next = ListNode(3)
    ptr = ptr.next
    ptr.next = ListNode(4)
    ptr = ptr.next
    ptr.next = ListNode(5)
    ptr = ptr.next
    test = Solution().reverseList(head)
    print(test.val)
