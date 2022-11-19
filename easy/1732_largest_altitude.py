# -*- coding: utf-8 -*-
# @Time    : 2022-11-19 9:09 a.m.
# @Author  : qkzhong
# @FileName: 1732_largest_altitude.py
# @Software: PyCharm
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        al = 0
        largest_al = 0
        for i in gain:
            al += i
            largest_al = max(largest_al, al)
        return largest_al