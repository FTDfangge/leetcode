# -*- coding: utf-8 -*-
# @Time    : 2022-03-24 4:52 p.m.
# @Author  : qkzhong
# @FileName: jianzhi56_I_single_numbers.py
# @Software: PyCharm

from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return list(s)


print(Solution().singleNumbers([4, 1, 4, 6]))
