# -*- coding: utf-8 -*-
# @Time    : 2022-03-12 3:24 p.m.
# @Author  : qkzhong
# @FileName: 154_min_in_rotated_array.py
# @Software: PyCharm
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = nums.__len__() - 1
        while left <= right:
            if nums[left] < nums[right]:
                return nums[left]
            else:
                mid = int((left + right) / 2)
                if nums[left] == nums[mid] and nums[mid] == nums[right]:
                    m = nums[left]
                    for i in range(left, right):
                        m = min(m, nums[i])
                    return m
                else:
                    if nums[mid] >= nums[left]:
                        # in the right hand
                        left = mid + 1
                    else:
                        # in the left hand
                        right = mid
        return nums[right]