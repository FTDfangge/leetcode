# -*- coding: utf-8 -*-
# @Time    : 2022-11-25 11:17 a.m.
# @Author  : qkzhong
# @FileName: 809_expressiveWords.py
# @Software: PyCharm
from typing import List


def is_expressive(s: str, target: str) -> bool:
    s_dict = []
    for i in s:
        if not s_dict:
            s_dict.append([i, 1])
            continue
        if s_dict[-1][0] == i:
            s_dict[-1][1] += 1
        else:
            s_dict.append([i, 1])
    t_dict = []
    for i in target:
        if not t_dict:
            t_dict.append([i, 1])
            continue
        if t_dict[-1][0] == i:
            t_dict[-1][1] += 1
        else:
            t_dict.append([i, 1])

    if s_dict.__len__() != t_dict.__len__():
        return False

    ptr = 0
    while ptr in range(s_dict.__len__()):
        if s_dict[ptr][0] == t_dict[ptr][0]:
            if s_dict[ptr][1] == t_dict[ptr][1]:
                ptr += 1
                continue
            elif s_dict[ptr][1] - t_dict[ptr][1] >= 0 and s_dict[ptr][1] >= 3:
                ptr += 1
                continue
            else:
                return False
        else:
            return False

    return True


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        count = 0
        for w in words:
            if is_expressive(s, w):
                count += 1
        return count


print(Solution().expressiveWords("dddiiiinnssssssoooo",
                                 ["dinnssoo", "ddinso", "ddiinnso", "ddiinnssoo", "ddiinso", "dinsoo", "ddiinsso",
                                  "dinssoo", "dinso"]))
