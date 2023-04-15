# -*- coding: utf-8 -*-
# @Time    : 2022-03-17 3:14 p.m.
# @Author  : qkzhong
# @FileName: jianzhi25_merge_sorted_list.py
# @Software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            ptr1 = l1
            ptr2 = l2
            if ptr1.val <= ptr2.val:
                head = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                head = ListNode(ptr2.val)
                ptr2 = ptr2.next
            ptr_new = head
            while ptr1 and ptr2:
                if ptr1.val <= ptr2.val:
                    ptr_new.next = ListNode(ptr1.val)
                    ptr_new = ptr_new.next
                    ptr1 = ptr1.next
                else:
                    ptr_new.next = ListNode(ptr2.val)
                    ptr_new = ptr_new.next
                    ptr2 = ptr2.next
            while ptr1:
                ptr_new.next = ListNode(ptr1.val)
                ptr_new = ptr_new.next
                ptr1 = ptr1.next
            while ptr2:
                ptr_new.next = ListNode(ptr2.val)
                ptr_new = ptr_new.next
                ptr2 = ptr2.next
            return head


if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    print(Solution().mergeTwoLists(list1, list2))