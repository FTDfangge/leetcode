# -*- coding: utf-8 -*-
# @Time    : 2021-11-262:38 p.m.
# @Author  : raynor
# @FileName: 461_hamming_distance.py
# @Software: PyCharm
def hammingWeight(n: int) -> int:
    ret = sum(1 for i in range(32) if n & (1 << i))
    return ret


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return hammingWeight((x ^ y))


if __name__ == '__main__':
    print(Solution().hammingDistance(1, 3))
