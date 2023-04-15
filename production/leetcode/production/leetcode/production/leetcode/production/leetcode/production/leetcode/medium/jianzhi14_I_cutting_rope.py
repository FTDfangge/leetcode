# -*- coding: utf-8 -*-
# @Time    : 2022-03-26 9:18 a.m.
# @Author  : qkzhong
# @FileName: jianzhi14_I_cutting_rope.py
# @Software: PyCharm

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2

        if n % 3 == 0:
            return pow(3, n//3)
        elif n % 3 == 1:
            return 4 * pow(3, (n-4)//3)
        elif n % 3 == 2:
            return 2 * pow(3, (n-2)//3)