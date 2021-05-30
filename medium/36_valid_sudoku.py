# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 3:40 p.m.
# @Author  : qkzhong
# @FileName: 36_valid_sudoku.py
# @Software: PyCharm

# AC 66.29% 57.19%

from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    # row
    for row in range(board.__len__()):
        hashtable = set()
        for element in board[row]:
            if element in hashtable and element != '.':
                return False
            elif element != '.':
                hashtable.add(element)

    # column
    for col in range(board[0].__len__()):
        hashtable = set()
        for index in range(9):
            if board[index][col] in hashtable and board[index][col] != '.':
                return False
            elif board[index][col] != '.':
                hashtable.add(board[index][col])

    # block
    for i in range(3):
        for j in range(3):
            hashtable = set()
            for index1 in range(3):
                for index2 in range(3):
                    if board[i * 3 + index1][j * 3 + index2] in hashtable and board[i * 3 + index1][j * 3 + index2] != '.':
                        return False
                    elif board[i * 3 + index1][j * 3 + index2] != '.':
                        hashtable.add(board[i * 3 + index1][j * 3 + index2])

    return True


if __name__ == '__main__':
    print(isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                            , ["8", ".", ".", "1", "9", "5", ".", ".", "."]
                            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
