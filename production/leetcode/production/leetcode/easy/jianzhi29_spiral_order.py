# -*- coding: utf-8 -*-
# @Time    : 2022-03-28 10:11 p.m.
# @Author  : qkzhong
# @FileName: jianzhi29_spiral_order.py
# @Software: PyCharm
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        visited = [[0 for i in range(matrix[0].__len__())] for j in range(matrix.__len__())]
        res = []

        def is_full_visited():
            for l in visited:
                if 0 in l:
                    return False
            return True

        x = 0
        y = 0
        res.append(matrix[y][x])
        visited[y][x] = 1
        while not is_full_visited():
            # go rightward
            while x < matrix[0].__len__() - 1 and visited[y][x + 1] == 0:
                x += 1
                res.append(matrix[y][x])
                visited[y][x] = 1

            # go downward
            while y < matrix.__len__() - 1 and visited[y + 1][x] == 0:
                y += 1
                res.append(matrix[y][x])
                visited[y][x] = 1

            # go leftward
            while x > 0 and visited[y][x - 1] == 0:
                x -= 1
                res.append(matrix[y][x])
                visited[y][x] = 1

            # go upward
            while y > 0 and visited[y - 1][x] == 0:
                y -= 1
                res.append(matrix[y][x])
                visited[y][x] = 1

        return res


print(Solution().spiralOrder( [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
