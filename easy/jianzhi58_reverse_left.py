# -*- coding: utf-8 -*-
# @Time    : 2022-03-11 8:28 p.m.
# @Author  : qkzhong
# @FileName: jianzhi58_reverse_left.py
# @Software: PyCharm

# AC

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        temp = s[::-1]
        front = temp[-1-n::-1]
        end = temp[:-1-n:-1]
        return front+end


if __name__ == '__main__':
    print(Solution().reverseLeftWords("abcdefg", 2))