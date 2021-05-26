# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 1:13 p.m.
# @Author  : qkzhong
# @FileName: 217_contains_duplicate.py
# @Software: PyCharm

# 96.59% 65.43%
def containsDuplicate(nums) -> bool:
    length = nums.__len__()
    if length > 1:
        dictionary = set()
        for i in range(nums.__len__()):
            if nums[i] in dictionary:
                return True
            else:
                dictionary.add(nums[i])
        return False

    else:
        return False


if __name__ == '__main__':
    print(containsDuplicate([1, 2, 3, 1]))
