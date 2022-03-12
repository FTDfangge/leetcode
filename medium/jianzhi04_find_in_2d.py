# -*- coding: utf-8 -*-
# @Time    : 2022-03-12 1:47 p.m.
# @Author  : qkzhong
# @FileName: jianzhi04_find_in_2d.py
# @Software: PyCharm

# AC
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix != []:
            top = 0
            right = matrix[0].__len__() - 1
            while top <= matrix.__len__() - 1 and right >= 0:
                if matrix[top][right] == target:
                    return True
                elif matrix[top][right] < target:
                    top += 1
                elif matrix[top][right] > target:
                    right -= 1
            return False
        else:
            return False


if __name__ == '__main__':
    print(Solution().findNumberIn2DArray([
    ],
        20))
