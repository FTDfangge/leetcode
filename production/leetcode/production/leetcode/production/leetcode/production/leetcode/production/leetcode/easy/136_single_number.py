# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 1:40 p.m.
# @Author  : qkzhong
# @FileName: 136_single_number.py
# @Software: PyCharm
from _ast import List

# AC

def singleNumber(nums) -> int:
    single = 0
    for i in range(nums.__len__()):
        single = single ^ nums[i]
    return single


if __name__ == '__main__':
    print(singleNumber([4, 1, 2, 1, 2]))
