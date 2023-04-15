# -*- coding: utf-8 -*-
# @Time    : 2021-11-262:42 p.m.
# @Author  : raynor
# @FileName: 190_reverse_bits.py
# @Software: PyCharm
class Solution:
    def reverseBits(self, n: int) -> int:
        str = ''
        for i in range(32):
            if (n & (1 << i)):
                str += '1'
            else:
                str += '0'
        return int(str, 2)


if __name__ == '__main__':
    print(Solution().reverseBits(0b11111111111111111111111111111101))