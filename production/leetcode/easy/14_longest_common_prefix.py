# -*- coding: utf-8 -*-
# @Time    : 2021-05-27 5:54 p.m.
# @Author  : qkzhong
# @FileName: 14_longest_common_prefix.py
# @Software: PyCharm

# AC but not best, not include Binary search
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if strs.__len__() == 0:
        return ''
    prefix = ''
    min_len = strs[0].__len__()
    for i in range(strs.__len__()):
        if strs[i].__len__() < min_len:
            min_len = strs[i].__len__()

    if min_len == 0:
        return ''

    for i in range(min_len):
        char = strs[0][i]
        for j in range(1, strs.__len__()):
            if strs[j][i] != char:
                return prefix
        prefix += char

    return prefix


if __name__ == '__main__':
    print(longestCommonPrefix(["flower", "flow", "flight"]))
