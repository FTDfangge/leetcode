# -*- coding: utf-8 -*-
# @Time    : 2022-03-26 10:03 a.m.
# @Author  : qkzhong
# @FileName: 682_baseball_game.py
# @Software: PyCharm
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        for op in ops:
            len = score.__len__()
            if op == '+':
                score.append(score[len - 2] + score[len - 1])
            elif op == 'D':
                score.append(2 * score[len - 1])
            elif op == 'C':
                score.pop()
            else:
                score.append(int(op))
        return sum(score)


print(Solution().calPoints(["5","2","C","D","+"]))