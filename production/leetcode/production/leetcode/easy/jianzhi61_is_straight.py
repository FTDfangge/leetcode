# -*- coding: utf-8 -*-
# @Time    : 2022-03-19 8:48 p.m.
# @Author  : qkzhong
# @FileName: jianzhi61_is_straight.py
# @Software: PyCharm

# AC

from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        zeros = 0
        if not nums:
            return True

        # step 1: find the first none zero
        while zeros in range(nums.__len__()):
            if nums[zeros] != 0:
                break
            zeros += 1

        # check forward
        f = zeros + 1
        while f in range(nums.__len__()):
            if nums[f] == nums[f-1]:
                return False
            if nums[f] != nums[f-1] +1:
                if zeros >= nums[f] - nums[f-1] - 1:
                    zeros -= nums[f] - nums[f-1] - 1
                else:
                    return False
            f += 1


        return True

if __name__ == '__main__':
    print(Solution().isStraight([0,0,9,4,5]))