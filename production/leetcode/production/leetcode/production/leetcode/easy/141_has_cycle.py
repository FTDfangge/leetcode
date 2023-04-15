# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 4:07 p.m.
# @Author  : qkzhong
# @FileName: 141_has_cycle.py
# @Software: PyCharm

class ListNode:
    __slots__ = ('val', 'next')

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


def hasCycle(head: ListNode) -> bool:
    dummy = ListNode(0, head)
    if head:
        rabbit = dummy.next
    else:
        return False
    turtle = dummy
    while rabbit != turtle:
        if rabbit.next:
            if rabbit.next.next:
                rabbit = rabbit.next.next
                turtle = turtle.next
            else:
                return False
        else:
            return False
    return True


if __name__ == '__main__':
    cycleNode = ListNode(3, ListNode(2, ListNode(0, ListNode(4))))
    cycleNode.next.next.next.next = cycleNode.next
    print(hasCycle(None))
