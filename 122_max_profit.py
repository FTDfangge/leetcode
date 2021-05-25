# -*- coding: utf-8 -*-
# @Time    : 2021-05-25 11:29 a.m.
# @Author  : qkzhong
# @FileName: 122_max_profit.py
# @Software: PyCharm
from _ast import List


def maxProfit(prices) -> int:
    profit = 0
    for i in range(1, prices.__len__()):
        profit += max(0, prices[i] - prices[i - 1])
    return profit


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
