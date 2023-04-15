# -*- coding: utf-8 -*-
# @Time    : 2022-11-27 10:34 a.m.
# @Author  : qkzhong
# @FileName: 1752_sorted_rotated.py
# @Software: PyCharm
import copy
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        original = copy.deepcopy(nums)
        original.sort()
        for i in range(nums.__len__()):
            last = nums[-1]
            nums = nums[:-1]
            nums.insert(0, last)
            if nums == original:
                return True
        return False


print(Solution().check(nums=[3, 4, 5, 1, 2]))
