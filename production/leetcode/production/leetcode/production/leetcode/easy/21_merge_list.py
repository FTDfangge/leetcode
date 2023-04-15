# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 1:43 p.m.
# @Author  : qkzhong
# @FileName: 21_merge_list.py
# @Software: PyCharm

class ListNode:
    __slots__ = ('val', 'next')

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_listNode(list) -> ListNode:
    dummy = ListNode(0)
    ptr = dummy
    for element in list:
        ptr.next = ListNode(element)
        ptr = ptr.next
    return dummy.next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    ptr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            ptr.next = ListNode(l1.val)
            ptr = ptr.next
            l1 = l1.next
        else:
            ptr.next = ListNode(l2.val)
            ptr = ptr.next
            l2 = l2.next
    while l1:
        ptr.next = ListNode(l1.val)
        ptr = ptr.next
        l1 = l1.next
    while l2:
        ptr.next = ListNode(l2.val)
        ptr = ptr.next
        l2 = l2.next
    return dummy.next


if __name__ == '__main__':
    mergeTwoLists(list_to_listNode([1, 2, 4]), list_to_listNode([1, 3, 4]))
