# -*- coding: utf-8 -*-
# @Time    : 2021-11-263:10 p.m.
# @Author  : raynor
# @FileName: 118_pascal's_triangle.py
# @Software: PyCharm
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(1, numRows + 1):
            triangle.append([])
            for j in range(1, i+1):
                if j == 1 or j == i:
                    triangle[i-1].append(1)
                else:
                    triangle[i-1].append(triangle[i-2][j-2] + triangle[i-2][j-1])
        return triangle



if __name__ == '__main__':
    print(Solution().generate(10))