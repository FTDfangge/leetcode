# -*- coding: utf-8 -*-
# @Time    : 2021-11-263:48 p.m.
# @Author  : raynor
# @FileName: 268_missing_number.py
# @Software: PyCharm
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        isExist = [1] * (nums.__len__() + 1)
        for i in range(nums.__len__()):
            if isExist[nums[i]]:
                isExist[nums[i]] = 0
        for i in range(isExist.__len__()):
            if isExist[i]:
                return i


if __name__ == '__main__':
    print(Solution().missingNumber([0, 1]))
