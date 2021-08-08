# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 10:44 a.m.
# @Author  : qkzhong
# @FileName: 237_delete_node.py
# @Software: PyCharm

# AC
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    while True:
        try:
            head = stringToListNode('[4,5,1,9]')
            node = 5

            ret = Solution().deleteNode(head.next)

            out = listNodeToString(head)
            if ret is not None:
                print("Do not return anything, modify head in-place instead.")
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
