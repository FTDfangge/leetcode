# -*- coding: utf-8 -*-
# @Time    : 2021-05-25 1:01 p.m.
# @Author  : qkzhong
# @FileName: 189_rotate.py
# @Software: PyCharm
from _ast import List


def rotate(nums, k: int):
    length = nums.__len__()
    k = k % length
    if length > 1:
        reverse(nums, 0, length-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, length-1)

    print(nums)


def reverse(nums, begin, end):
    back = 0
    for i in range(begin, begin + ((end - begin) // 2) + 1):
        nums[i], nums[end - back] = nums[end - back], nums[i]
        back += 1


if __name__ == '__main__':
    rotate([1, 2], 3)
