# -*- coding: utf-8 -*-
# @Time    : 2021-06-04 1:59 p.m.
# @Author  : qkzhong
# @FileName: 70_climb_stairs.py
# @Software: PyCharm

# AC

class Solution:
    def climbStairs(self, n: int) -> int:
        # f(x) = f(x - 1) + f(x - 2)
        # f0=1
        # f1=1
        p = 0
        q = 0
        r = 1
        for i in range(n):
            p = q
            q = r
            r = p + q
        return r


if __name__ == '__main__':
    print(Solution().climbStairs(38))
