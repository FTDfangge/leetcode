# -*- coding: utf-8 -*-
# @Time    : 2022-03-17 6:09 p.m.
# @Author  : qkzhong
# @FileName: jianzhi58_I_reverse_words.py
# @Software: PyCharm

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        reverse_all = s[::-1]
        output = ""
        c = 0
        begin = 0
        end = 0
        while c in range(reverse_all.__len__()):
            if reverse_all[c] != ' ':
                end = end + 1
            else:
                # meet the space
                output += reverse_all[begin: end: 1][::-1]
                # count the space and add nothing if it is the begin, or add 1 space
                while reverse_all[c] == ' ':
                    c += 1
                    if c >= reverse_all.__len__():
                        if output:
                            if output[0] == ' ':
                                output = output[1::]
                        return output

                output += ' '
                begin = c
                end = c + 1
            c += 1
        output += reverse_all[begin: end : 1][::-1]

        if output:
            if output[0] == ' ':
                output = output[1::]
        return output


if __name__ == '__main__':
    print(Solution().reverseWords(" "))
