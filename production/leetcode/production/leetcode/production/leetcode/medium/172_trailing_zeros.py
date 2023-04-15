# -*- coding: utf-8 -*-
# @Time    : 2022-03-25 4:49 p.m.
# @Author  : qkzhong
# @FileName: 172_trailing_zeros.py
# @Software: PyCharm
import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_of_zero = 0
        fac = math.factorial(n)
        while fac % 10 == 0:
            fac //= 10
            num_of_zero += 1
        return num_of_zero

    def trailingZeroes2(self, n: int) -> int:
        num_of_five = 0
        if n < 5:
            return 0
        temp = n
        while temp % 5 == 0:
            temp //= 5
            num_of_five += 1
        print(n, num_of_five)
        if n % 5 !=0:
            return self.trailingZeroes2(n-n%5)
        else:
            return num_of_five + self.trailingZeroes2(n - 5)


print(Solution().trailingZeroes2(26))