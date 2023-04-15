# -*- coding: utf-8 -*-
# @Time    : 2021-05-27 10:10 a.m.
# @Author  : qkzhong
# @FileName: 7_reverse_integer.py
# @Software: PyCharm

# AC 97.65% 74.77%

def reverse(x: int) -> int:
    if x > 0:
        new_int = 0
        while x != 0:
            new_int = new_int * 10 + x % 10
            x = x // 10
    else:
        x = -x
        new_int = 0
        while x != 0:
            new_int = new_int * 10 + x % 10
            x = x // 10
        new_int = -new_int

    if new_int >= pow(2, 31) or new_int < -pow(2, 31):
        return 0

    return new_int


if __name__ == '__main__':
    print(reverse(1534236469))
