# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 2:54 p.m.
# @Author  : qkzhong
# @FileName: 1_two_sum.py
# @Software: PyCharm
from typing import List


# AC but time spent is too long
def twoSum(nums: List[int], target: int) -> List[int]:
    for slow in range(nums.__len__()):
        for quick in range(slow + 1, nums.__len__()):
            if nums[slow] + nums[quick] == target:
                return [slow, quick]


# AC 68.73% 5.09%
def twoSum_new(nums: List[int], target: int) -> List[int]:
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []


if __name__ == '__main__':
    print(twoSum_new([1, 2, 7, 11, 15], 9))
