# -*- coding: utf-8 -*-
# @Time    : 2022-03-18 4:06 p.m.
# @Author  : qkzhong
# @FileName: 79_word_search.py
# @Software: PyCharm
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, k):
            if not x in range(board.__len__()) or not y in range(board[0].__len__()) or board[x][y] != word[k]:
                # out of matrix or not the correct letter
                return False
            if k == word.__len__() - 1:
                # the last letter
                return True
            # the current is used, set it to null
            board[x][y] = ''
            # explore every direction
            output = dfs(x - 1, y, k + 1) or dfs(x, y - 1, k + 1) or dfs(x + 1, y, k + 1) or dfs(x, y + 1, k + 1)
            # the current is released
            board[x][y] = word[k]
            return output

        for i in range(board.__len__()):
            for j in range(board[0].__len__()):
                if dfs(i, j, 0):
                    return True
        return False