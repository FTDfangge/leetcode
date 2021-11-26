# -*- coding: utf-8 -*-
# @Time    : 2021-11-263:27 p.m.
# @Author  : raynor
# @FileName: 20_valid_parentheses.py
# @Software: PyCharm
from typing import List


class Solution:
    def myPop(self, stack: List, element) -> bool:
        if element == "}":
            element = "{"
        elif element == "]":
            element = "["
        elif element == ")":
            element = "("

        if stack.__len__() > 0:
            if stack[stack.__len__() - 1] == element:
                stack.pop()
                return True

        return False

    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not self.myPop(stack, i):
                    return False

        if stack.__len__() == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isValid('{}[()]'))
