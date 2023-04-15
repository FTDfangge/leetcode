# -*- coding: utf-8 -*-
# @Time    : 2022-03-16 9:04 p.m.
# @Author  : qkzhong
# @FileName: jianzhi48_length_of_longest_substring.py
# @Software: PyCharm


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # this do not work at like test case: "dvdf"
        if s.__len__() == 0:
            return 0

        ptr = 0
        length = 0
        longest = 1
        c = set()
        while ptr < s.__len__():
            if not s[ptr] in c:
                length += 1
                c.add(s[ptr])
            else:
                if length >= longest:
                    longest = length
                length = 1
                c = set()
                c.add(s[ptr])
            ptr += 1

        if length >= longest:
            longest = length
        return longest

    def lengthOfLongestSubstring2(self, s: str) -> int:
        # AC but not time efficient
        if s.__len__() == 0:
            return 0
        start_ptr = 0
        longest = 0
        while start_ptr < s.__len__():
            offset = 0
            length = 0
            c = set()
            while start_ptr + offset < s.__len__():
                if not s[start_ptr + offset] in c:
                    length += 1
                    c.add(s[start_ptr + offset])
                else:
                    break
                offset += 1
            if length >= longest:
                longest = length
            start_ptr += 1
        return longest



if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring2("dvdf"))
