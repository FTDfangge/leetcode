# -*- coding: utf-8 -*-
# @Time    : 2022-03-17 4:46 p.m.
# @Author  : qkzhong
# @FileName: jianzhi21_exchange.py
# @Software: PyCharm
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        ptr_front = 0
        ptr_back = nums.__len__() - 1

        while ptr_front < ptr_back:
            # front move to the first even number
            while nums[ptr_front] % 2 != 0 and ptr_front < ptr_back:
                ptr_front += 1
            # back move to the first odd number
            while nums[ptr_back] % 2 == 0 and ptr_front < ptr_back:
                ptr_back -= 1

            if ptr_front < ptr_back:
                temp = nums[ptr_front]
                nums[ptr_front] = nums[ptr_back]
                nums[ptr_back] = temp

        return nums