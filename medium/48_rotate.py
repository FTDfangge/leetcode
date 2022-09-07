# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 5:47 p.m.
# @Author  : qkzhong
# @FileName: 48_rotate.py
# @Software: PyCharm

# AC 94.79% 76.64%

from typing import List

'''
row, col -> col, num-row-1
col, num-row-1 -> num-row-1, num-col-1
num-row-1, num-col-1 -> num-col-1, num-(num-row-1)-1=row
num-col-1, row -> row, col
'''


def rotate(matrix: List[List[int]]) -> None:
    n = matrix.__len__()
    if n % 2 == 0:
        for row in range(n//2):
            for col in range(n//2):
                matrix[col][n - row - 1], matrix[n - row - 1][n - col - 1], matrix[n - col - 1][row], matrix[row][col] = \
                    matrix[row][col], matrix[col][n - row - 1], matrix[n - row - 1][n - col - 1], matrix[n - col - 1][row]
    else:
        for row in range(n//2 + 1):
            for col in range(n//2):
                matrix[col][n - row - 1], matrix[n - row - 1][n - col - 1], matrix[n - col - 1][row], matrix[row][col] = \
                    matrix[row][col], matrix[col][n - row - 1], matrix[n - row - 1][n - col - 1], matrix[n - col - 1][row]
    print(matrix)


if __name__ == '__main__':
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    for i in range(10):
        rotate(matrix)

