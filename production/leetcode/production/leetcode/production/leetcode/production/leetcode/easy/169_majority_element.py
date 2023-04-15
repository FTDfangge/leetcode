# -*- coding: utf-8 -*-
# @Time    : 2022-03-25 4:11 p.m.
# @Author  : qkzhong
# @FileName: 169_majority_element.py
# @Software: PyCharm

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

            if d[i] > (nums.__len__() // 2):
                return i