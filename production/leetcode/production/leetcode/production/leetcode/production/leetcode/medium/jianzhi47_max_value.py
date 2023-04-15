# -*- coding: utf-8 -*-
# @Time    : 2022-03-15 9:58 p.m.
# @Author  : qkzhong
# @FileName: jianzhi47_max_value.py
# @Software: PyCharm
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        def dp(x: int, y: int) -> int:
            if [x, y] == [0, 0]:
                return grid[x][y]
            elif x == 0:
                return dp(x, y - 1) + grid[x][y]
            elif y == 0:
                return dp(x - 1, y) + grid[x][y]
            else:
                return max(dp(x, y - 1) + grid[x][y], dp(x - 1, y) + grid[x][y])

        return dp(grid.__len__() - 1, grid[0].__len__() - 1)

    def maxValueMatrix(self, grid: List[List[int]]) -> int:
        maxvalue = [[0] * grid[0].__len__()] * grid.__len__()
        for x in range(grid.__len__()):
            for y in range(grid[0].__len__()):

                if [x, y] == [0, 0]:
                    maxvalue[x][y] = grid[0][0]
                elif x == 0:
                    maxvalue[x][y] = maxvalue[x][y - 1] + grid[x][y]
                elif y == 0:
                    maxvalue[x][y] = maxvalue[x - 1][y] + grid[x][y]
                else:
                    maxvalue[x][y] = max(maxvalue[x][y - 1] + grid[x][y], maxvalue[x - 1][y] + grid[x][y])

        return maxvalue[grid.__len__() - 1][grid[0].__len__() - 1]


if __name__ == '__main__':
    print(Solution().maxValue([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
