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

        for index in range(1, dic.__len__(), 2):
            if dic[index] == 1:
                return dic[index - 1]

        return ' '


class Solution2:
    def firstUniqChar(self, s: str) -> str:
        position = dict()
        n = len(s)
        for i, ch in enumerate(s):
            if ch in position:
                position[ch] = -1
            else:
                position[ch] = i
        first = n
        for pos in position.values():
            if pos != -1 and pos < first:
                first = pos
        return ' ' if first == n else s[first]


if __name__ == '__main__':
    print(Solution2().firstUniqChar('leetcode'))
