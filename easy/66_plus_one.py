# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 2:19 p.m.
# @Author  : qkzhong
# @FileName: 66_plus_one.py
# @Software: PyCharm

# AC

def plusOne(digits):
    i = digits.__len__() - 1
    while i >= 0:
        digits[i] += 1
        digits[i] %= 10
        if not digits[i] == 0:
            return digits
        i -= 1
    return [1] + digits


if __name__ == '__main__':
    print(plusOne([4, 9, 9, 9, 9, 9]))
