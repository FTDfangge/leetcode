# -*- coding: utf-8 -*-
# @Time    : 2022-03-14 8:33 p.m.
# @Author  : qkzhong
# @FileName: jianzhi10_I_fib.py
# @Software: PyCharm

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

    def fib2(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            p = 0
            q = 0
            r = 1
            for i in range(1, n):
                p = q
                q = r
                r = p + q

            return r


if __name__ == '__main__':
    print(Solution().fib(5))