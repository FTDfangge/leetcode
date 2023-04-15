# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 2:03 p.m.
# @Author  : qkzhong
# @FileName: 234_palindrome.py
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


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()


if __name__ == '__main__':
    print(Solution().isPalindrome(list_to_listNode([1, 2, 3, 4, 6, 4, 3, 2, 1])))
