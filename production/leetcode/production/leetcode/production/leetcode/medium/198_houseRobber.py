# -*- coding: utf-8 -*-
# @Time    : 2021-11-087:09 p.m.
# @Author  : raynor
# @FileName: 198_houseRobber.py
# @Software: PyCharm

#AC

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(x)为前x家能偷的最多金额
        # f(x) = max(f(x-2)+nums[i], f(x-1))
        # f0 = 0
        # f1 = nums[0]
        money = [0] * nums.__len__()
        money[0] = nums[0]
        if (nums.__len__() > 1):
            money[1] = max(nums[0], nums[1])
            for i in range(2, nums.__len__()):
                money[i] = max(money[i - 2] + nums[i], money[i - 1])
        return money[nums.__len__() - 1]


if __name__ == '__main__':
    print(Solution().rob([2, 7, 9, 3, 1]))
