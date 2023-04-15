# -*- coding: utf-8 -*-
# @Time    : 2022-03-14 8:58 p.m.
# @Author  : qkzhong
# @FileName: jianzhi63_max_profit.py
# @Software: PyCharm

# AC

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def max_before_i(index : int) -> int:
            if index < 1:
                return 0
            else:
                return max(max_before_i(index - 1), prices[index] - min(prices[0:index]))

        return max_before_i(prices.__len__() -1)


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))