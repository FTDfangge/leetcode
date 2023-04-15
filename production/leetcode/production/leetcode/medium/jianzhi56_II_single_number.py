# -*- coding: utf-8 -*-
# @Time    : 2022-03-24 5:02 p.m.
# @Author  : qkzhong
# @FileName: jianzhi56_II_single_number.py
# @Software: PyCharm
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                if d[i] < 2:
                    d[i] += 1
                else:
                    d.pop(i)
        return int(d.popitem()[0])