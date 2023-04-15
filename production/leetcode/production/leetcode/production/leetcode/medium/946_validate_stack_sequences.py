# -*- coding: utf-8 -*-
# @Time    : 2022-03-28 10:56 p.m.
# @Author  : qkzhong
# @FileName: 946_validate_stack_sequences.py
# @Software: PyCharm

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        ptr_push = 0
        ptr_pop = 0
        for ptr_push in range(pushed.__len__()):
            while stack and stack[stack.__len__() - 1] == popped[ptr_pop]:
                stack.pop()
                ptr_pop += 1
            stack.append(pushed[ptr_push])

        while stack and stack[stack.__len__() - 1] == popped[ptr_pop]:
            stack.pop()
            ptr_pop += 1

        if stack:
            return False
        else:
            return True


print(Solution().validateStackSequences([1,2,3,4,5], [4,5,3,1,2]))