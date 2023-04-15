# -*- coding: utf-8 -*-
# @Time    : 2022-03-18 4:20 p.m.
# @Author  : qkzhong
# @FileName: jianzhi13_moving_count.py
# @Software: PyCharm

import numpy as np


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        matrix = [[0 for i in range(n)] for i in range(m)]


        def dfs_count(x, y, kk) -> int:
            if not x in range(m) or not y in range(n) or get_sum(x) + get_sum(y) > kk or matrix[x][y] != 0:
                # not permit
                return 0
            matrix[x][y] = 1

            return 1 + dfs_count(x - 1, y, kk) + dfs_count(x, y - 1, kk) + \
                   dfs_count(x + 1, y, kk) + dfs_count(x, y + 1, kk)

        def get_sum(a: int) -> int:
            sum = 0
            while a > 0:
                sum += a % 10
                a = a // 10
            return sum

        return dfs_count(0, 0, k)


if __name__ == '__main__':
    print(Solution().movingCount(3, 2, 17))

