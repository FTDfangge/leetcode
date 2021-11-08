# -*- coding: utf-8 -*-
# @Time    : 2021-11-089:49 p.m.
# @Author  : raynor
# @FileName: 326_power_of_three.py
# @Software: PyCharm

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False

        if n % 1 != 0:
            return False
        if n == 1:
            return True
        n = n / 3
        return self.isPowerOfThree(n)


if __name__ == '__main__':
    print(Solution().isPowerOfThree(0))
