# -*- coding: utf-8 -*-
# @Time    : 2022-03-11 4:22 p.m.
# @Author  : qkzhong
# @FileName: jianzhi35_copy_random_list.py
# @Software: PyCharm

# AC

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head:
            ptr = head
            while ptr:
                temp_next = ptr.next
                ptr.next = Node(ptr.val, temp_next, ptr.random)
                ptr = ptr.next.next

            ptr = head.next
            while ptr.next:
                ptr.next = ptr.next.next
                if ptr.random:
                    ptr.random = ptr.random.next
                ptr = ptr.next
            if ptr.random:
                ptr.random = ptr.random.next
            return head.next
        else:
            return None


if __name__ == '__main__':
    # head = Node(7, Node(13, Node(11, Node(10, Node(1, None, None), None), None), None), None)
    # head.next.random = head
    # head.next.next.random = head.next.next.next.next
    # head.next.next.next.random = head.next.next
    # head.next.next.next.next.random = head

    head = Node(1, Node(2, None, None), None)
    head.random = head.next
    head.next.random = head.next

    output = Solution().copyRandomList(head)
    print()