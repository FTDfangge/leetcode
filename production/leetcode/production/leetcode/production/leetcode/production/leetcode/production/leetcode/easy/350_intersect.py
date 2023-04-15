# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 1:57 p.m.
# @Author  : qkzhong
# @FileName: 350_intersect.py
# @Software: PyCharm

# AC

import collections


def intersect(nums1, nums2):
    hash_table = collections.Counter()
    for i in nums1:
        hash_table[i] += 1

    result = list()
    for i in nums2:
        if hash_table.get(i):
            result.append(i)
            hash_table[i] -= 1
            if hash_table[i] == 0:
                hash_table.pop(i)
    return result


if __name__ == '__main__':
    print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
