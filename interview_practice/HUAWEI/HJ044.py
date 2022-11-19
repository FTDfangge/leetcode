# -*- coding: utf-8 -*-
# @Time    : 2022-09-10 11:52 p.m.
# @Author  : qkzhong
# @FileName: HJ044.py
# @Software: PyCharm

def dfs(matrix) -> bool:
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                s = find_possibilities(i, j)  # 可能的集合
                for k in s:
                    matrix[i][j] = k
                    if dfs(matrix):
                        return True
                matrix[i][j] = 0
                return False
    return True


def find_possibilities(x, y):
    could = [1] * 9
    # 横行排除可能
    for j in range(9):
        if matrix[x][j] != 0:
            could[matrix[x][j] - 1] = 0
    # 竖列排除可能
    for i in range(9):
        if matrix[i][y] != 0:
            could[matrix[i][y] - 1] = 0
    # 3*3排除可能
    for i in range(3 * (x // 3), 3 * (x // 3) + 3):
        for j in range(3 * (y // 3), 3 * (y // 3) + 3):
            if matrix[i][j] != 0:
                could[matrix[i][j] - 1] = 0
    s = set()
    for i in range(could.__len__()):
        if could[i] == 1:
            s.add(i + 1)
    return s


matrix = [[0] * 9 for _ in range(9)]
for i in range(9):
    matrix[i] = list(map(int, input().split(' ')))
dfs(matrix)
for i in range(9):
    s = ''
    for j in range(9):
        s += str(matrix[i][j]) + ' '
    s.rstrip(' ')
    print(s)

