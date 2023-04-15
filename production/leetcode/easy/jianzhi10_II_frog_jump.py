# -*- coding: utf-8 -*-
# @Time    : 2022-03-14 8:47 p.m.
# @Author  : qkzhong
# @FileName: jianzhi10_II_frog_jump.py
# @Software: PyCharm

class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            p = 0
            q = 1
            r = 1
            for i in range(1, n):
                p = q
                q = r
                r = p + q
            return r


if __name__ == '__main__':
    print(Solution().numWays(5))
