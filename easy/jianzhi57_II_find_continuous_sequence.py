# -*- coding: utf-8 -*-
# @Time    : 2022-03-26 9:27 a.m.
# @Author  : qkzhong
# @FileName: jianzhi57_II_find_continuous_sequence.py
# @Software: PyCharm
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        l = 1
        r = 2
        while l < r < target:
            sum = (l + r) * (r - l + 1) / 2
            if sum == target:
                res.append(list(range(l, r + 1)))
                l += 1
            elif sum < target:
                r += 1
            elif sum > target:
                l += 1
        return res


for i in range(1, 1000):
    print(i, Solution().findContinuousSequence(i))
