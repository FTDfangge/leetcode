# -*- coding: utf-8 -*-
# @Time    : 2022-03-17 5:43 p.m.
# @Author  : qkzhong
# @FileName: jianzhi57_two_sum.py
# @Software: PyCharm

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        front = 0
        back = nums.__len__() - 1
        while front < back:
            if nums[front] + nums[back] > target:
                # move back ptr forward
                back -= 1
            elif nums[front] + nums[back] < target:
                # move front ptr backward
                front += 1
            else:
                return [nums[front], nums[back]]
