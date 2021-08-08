# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 1:16 p.m.
# @Author  : qkzhong
# @FileName: 206_reverse_list.py
# @Software: PyCharm

# AC

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_listNode(list) -> ListNode:
    dummy = ListNode()
    ptr = dummy
    for element in list:
        ptr.next = ListNode(element)
        ptr = ptr.next
    return dummy.next


def reverseList(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    pre = None
    current = dummy.next
    while current:
        next = current.next
        current.next = pre
        pre = current
        current = next
    return pre


if __name__ == '__main__':
    reverseList(list_to_listNode([1, 2, 3, 4, 5]))
