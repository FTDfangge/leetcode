# -*- coding: utf-8 -*-
# @Time    : 2022-03-28 3:53 p.m.
# @Author  : qkzhong
# @FileName: 693_has_alternating_bits.py
# @Software: PyCharm

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre = int(not n % 2)
        while n != 0:
            if n % 2 == pre:
                return False
            pre = n % 2
            n //= 2
        return True


print(Solution().hasAlternatingBits(11))