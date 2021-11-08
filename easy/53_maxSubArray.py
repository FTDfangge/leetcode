# -*- coding: utf-8 -*-
# @Time    : 2021-11-08 1:59 p.m.
# @Author  : qkzhong
# @FileName: 53_maxSubArray.py
# @Software: PyCharm

# AC

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # f(x)为代表以第 x 个数结尾的
        # fx = max(nums[x], fx-1+nums[x])
        # f0 = 0
        # f1 = nums[0]
        f = [0] * nums.__len__()
        f[0] = nums[0]
        if nums.__len__() > 1:
            for i in range(1, nums.__len__()):
                f[i] = max(nums[i], f[i - 1] + nums[i])

        return max(f)


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
