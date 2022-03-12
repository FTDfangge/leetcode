# -*- coding: utf-8 -*-
# @Time    : 2022-03-12 3:59 p.m.
# @Author  : qkzhong
# @FileName: jianzhi50_first_uniq_char.py
# @Software: PyCharm

# AC

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = []
        for c in s:
            if c not in dic:
                dic.append(c)
                dic.append(1)
            else:
                dic[dic.index(c) + 1] += 1

        for index in range(1, dic.__len__(),2):
            if dic[index] == 1:
                return dic[index - 1]

        return ' '


if __name__ == '__main__':
    print(Solution().firstUniqChar('leetcode'))