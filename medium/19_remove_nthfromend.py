# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 11:17 a.m.
# @Author  : qkzhong
# @FileName: 19_remove_nthfromend.py
# @Software: PyCharm

# AC

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_listNode(list):
    dummy_root = ListNode(0)
    ptr = dummy_root
    for element in list:
        ptr.next = ListNode(element)
        ptr = ptr.next
    return dummy_root.next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    first = head
    second = dummy
    for i in range(n):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy.next


if __name__ == '__main__':
    listNode = removeNthFromEnd(list_to_listNode([1, 2, 3, 4, 5]), 3)
    while listNode:
        print(listNode.val)
        listNode = listNode.next
