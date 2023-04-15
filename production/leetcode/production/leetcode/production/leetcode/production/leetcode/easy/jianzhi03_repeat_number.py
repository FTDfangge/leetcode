# -*- coding: utf-8 -*-
# @Time    : 2022-03-11 2:23 p.m.
# @Author  : qkzhong
# @FileName: jianzhi03_repeat_number.py
# @Software: PyCharm
from typing import List

#AC
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        recorder = [0] * nums.__len__()
        for num in nums:
            if recorder[num - 1] == 1:
                return num
            else:
                recorder[num - 1] += 1


if __name__ == '__main__':
    print(Solution().findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))