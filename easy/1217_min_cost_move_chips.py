# -*- coding: utf-8 -*-
# @Time    : 2022-07-08 9:48 a.m.
# @Author  : qkzhong
# @FileName: 1217_min_cost_move_chips.py
# @Software: PyCharm
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = even = 0
        for i in position:
            if i % 2 == 1:
                odd += 1
            else:
                even += 1
        return min(odd, even)

if __name__ == '__main__':
    print(Solution().minCostToMoveChips([2,2,2,3,3]))
