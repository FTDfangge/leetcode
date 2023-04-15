# -*- coding: utf-8 -*-
# @Time    : 2022-03-20 4:20 p.m.
# @Author  : qkzhong
# @FileName: jianzhi64_sum_nums.py
# @Software: PyCharm

# AC

class Solution:
    def sumNums(self, n: int) -> int:
        return n and n+self.sumNums(n-1)


if __name__ == '__main__':
    print(Solution().sumNums(3))