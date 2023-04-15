# -*- coding: utf-8 -*-
# @Time    : 2022-03-11 9:00 p.m.
# @Author  : qkzhong
# @FileName: jianzhi53_II_missing_number.py
# @Software: PyCharm
# AC

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        right = nums.__len__() - 1
        while left <= right:
            mid = int((left + right) / 2)
            if mid != nums[mid]:
                # in the front
                right = mid - 1
            else:
                # in the back
                left = mid + 1
        if left > right:
            return left
        else:
            return int((left + right) / 2)


if __name__ == '__main__':
    print(Solution().missingNumber([0,1,2,3,5,6]))
