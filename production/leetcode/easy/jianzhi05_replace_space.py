# -*- coding: utf-8 -*-
# @Time    : 2022-03-11 8:17 p.m.
# @Author  : qkzhong
# @FileName: jianzhi05_replace_space.py
# @Software: PyCharm

# AC

class Solution:
    def replaceSpace(self, s: str) -> str:
        output = ""
        for c in s:
            if c != " ":
                output += c
            else:
                output += "%20"
        return output


if __name__ == '__main__':
    print(Solution().replaceSpace("Hello world test"))
