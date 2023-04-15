# -*- coding: utf-8 -*-
# @Time    : 2021-11-262:06 p.m.
# @Author  : raynor
# @FileName: 191_numof1bits.py
# @Software: PyCharm
class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret


if __name__ == '__main__':
    print(Solution().hammingWeight(0b1011))
