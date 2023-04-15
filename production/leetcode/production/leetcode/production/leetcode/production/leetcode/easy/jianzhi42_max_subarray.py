# -*- coding: utf-8 -*-
# @Time    : 2022-03-15 9:15 p.m.
# @Author  : qkzhong
# @FileName: jianzhi42_max_subarray.py
# @Software: PyCharm
from math import inf

# AC
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f = [0] * nums.__len__()
        f[0] = nums[0]
        if nums.__len__() > 1:
            for i in range(1, nums.__len__()):
                f[i] = max(nums[i], f[i - 1] + nums[i])
                print(f[i])

        return max(f)


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
