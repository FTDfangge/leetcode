# -*- coding: utf-8 -*-
# @Time    : 2022-03-23 4:39 p.m.
# @Author  : qkzhong
# @FileName: jianzhi15_hamming_weight.py
# @Software: PyCharm

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            if n % 2 == 1:
                res += 1
            n //= 2
        return res


print(Solution().hammingWeight(0b111))
