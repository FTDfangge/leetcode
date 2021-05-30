# -*- coding: utf-8 -*-
# @Time    : 2021-05-27 3:15 p.m.
# @Author  : qkzhong
# @FileName: 28_strstr.py
# @Software: PyCharm

# AC but slow
def strStr(haystack: str, needle: str) -> int:
    def find_next_begin(inner_begin, inner_haystack, inner_needle):
        inner_begin += 1
        for inner_begin in range(inner_begin, inner_haystack.__len__()):
            if inner_haystack[inner_begin] == inner_needle[0]:
                if inner_haystack.__len__() - inner_begin < inner_needle.__len__():
                    return -1
                break
            elif inner_begin == inner_haystack.__len__() - 1 and inner_haystack != inner_needle[0]:
                return -1
        return inner_begin

    if haystack.__len__() < needle.__len__():
        return -1
    elif needle.__len__() == 0:
        return 0
    begin = 0
    for begin in range(begin, haystack.__len__()):
        if haystack[begin] == needle[0]:
            if haystack.__len__() - begin < needle.__len__():
                return -1
            break
        elif begin == haystack.__len__() - 1 and haystack != needle[0]:
            return -1
    needle_pointer = 0
    while needle_pointer in range(needle.__len__()):
        if haystack[begin + needle_pointer] != needle[needle_pointer]:
            begin = find_next_begin(begin, haystack, needle)
            if begin == -1:
                return -1
            needle_pointer = -1
        needle_pointer += 1

    return begin


def strStr_new(haystack: str, needle: str) -> int:
    def kmp(hstr, lenh, nstr, lenn):
        n = next(nstr, lenn)
        j = 0
        for i in range(lenh):
            while j > 0 and hstr[i] != nstr[j]:
                j = n[j - 1] + 1
                if lenn - j + i > lenh:
                    return -1

    def next(nstr, lenn):
        nextt = [-2] * lenn
        nextt[0] = -1
        k = -1
        for i in range(lenn):
            while k != -1 and nstr[k + 1] != nstr[i]:
                k = nextt[k]
            if nstr[k + 1] == nstr[i]:
                k += 1
            nextt[i] = k
        return nextt

    if needle.__len__() == 0:
        return 0
    if haystack.__len__() == 0:
        return -1
    return kmp(haystack, haystack.__len__(), needle, needle.__len__())


if __name__ == '__main__':
    print(strStr_new('mississipi', 'issip'))
