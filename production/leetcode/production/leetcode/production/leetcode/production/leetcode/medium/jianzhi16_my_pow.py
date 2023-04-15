# -*- coding: utf-8 -*-
# @Time    : 2022-03-23 1:59 p.m.
# @Author  : qkzhong
# @FileName: jianzhi16_my_pow.py
# @Software: PyCharm

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            res = 1.0
            p = x
            for num in bin(n)[::-1]:
                if num == 'b':
                    break
                if int(num):
                    res *= p
                p *= p
            return res

        else:
            res = 1.0
            p = x
            for num in bin(n)[::-1]:
                if num == 'b':
                    break
                if int(num):
                    res *= p
                p *= p
            return 1/res


print(Solution().myPow(2, -5))
