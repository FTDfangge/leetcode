# -*- coding: utf-8 -*-
# @Time    : 2021-05-27 10:03 a.m.
# @Author  : qkzhong
# @FileName: 344_reverse_string.py
# @Software: PyCharm

# AC

from typing import List


def reverseString(s: List[str]) -> None:
    length = s.__len__()
    for i in range(length // 2):
        s[i], s[length - i - 1] = s[length - i - 1], s[i]


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(s)
