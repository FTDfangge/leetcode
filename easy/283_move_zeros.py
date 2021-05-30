# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 2:42 p.m.
# @Author  : qkzhong
# @FileName: 283_move_zeros.py
# @Software: PyCharm

# AC 99.55% 61.55%

from typing import List


def moveZeroes(nums: List[int]) -> None:
    new_i = 0
    for i in range(nums.__len__()):
        if nums[i] != 0:
            nums[new_i] = nums[i]
            new_i += 1

    while new_i < nums.__len__():
        nums[new_i] = 0
        new_i += 1

    print(nums)


if __name__ == '__main__':
    moveZeroes([0, 1, 0, 3, 12])
