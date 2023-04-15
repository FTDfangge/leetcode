# -*- coding: utf-8 -*-
# @Time    : 2021-05-27 1:40 p.m.
# @Author  : qkzhong
# @FileName: 8_myatoi.py
# @Software: PyCharm


# AC 48.30% 16.64% better than leetcode answer
def myAtoi(s: str) -> int:
    if s.__len__() == 0:
        return 0
    else:
        head = 0
        digit_read = False
        integer = 0
        pre = ''
        n = s.__len__()

        # delete the pre blank
        while s[head] == ' ':
            head += 1
            if head >= n:
                return integer

        # find the pre or exit
        while not digit_read and head < n:
            if s[head].isdigit():
                digit_read = True
            elif (s[head] == '+' or s[head] == '-') and pre == '':
                pre = s[head]
                head += 1
            else:
                return 0

        # head is the num
        while digit_read and head < n:
            if s[head].isdigit():
                integer = integer * 10 + int(s[head])
                head += 1
            else:
                if pre == '-':
                    integer = -integer
                return max(min(integer, pow(2, 31) - 1), -pow(2, 31))
        if pre == '-':
            integer = -integer
        return max(min(integer, pow(2, 31) - 1), -pow(2, 31))


if __name__ == '__main__':
    print(myAtoi("   -42"))
