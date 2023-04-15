# -*- coding: utf-8 -*-
# @Time    : 2022-11-20 9:36 p.m.
# @Author  : qkzhong
# @FileName: 799_champagne_tower.py
# @Software: PyCharm
from typing import List


def pour_into_tower(tower: List[List[float]], n, row, col):  # 向塔里倒n杯， 判断要查询的是否满
    # 向顶部倒n杯
    tower[0][0] += n
    for level in range(row):
        for idx in range(tower[level].__len__()):
            if tower[row][col] >= 1:
                return 1
            if tower[level][idx] > 1:
                # 向两边流
                tower[level + 1][idx] += (tower[level][idx] - 1) / 2
                tower[level + 1][idx + 1] += (tower[level][idx] - 1) / 2
                if tower[level + 1][idx] >= 1 and level + 1 == row and idx == col:
                    return 1
                elif tower[level + 1][idx + 1] >= 1 and level + 1 == row and idx + 1 == col:
                    return 1
                tower[level][idx] = 1.0
    return 0


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = []
        for i in range(1, query_row + 2):
            tower.append([0.0] * i)
        if pour_into_tower(tower, poured, query_row, query_glass):
            return 1
        return min(1.0, tower[query_row][query_glass])


print(Solution().champagneTower(25, 6, 1))
