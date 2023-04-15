# -*- coding: utf-8 -*-
# @Time    : 2022-09-07 3:32 p.m.
# @Author  : qkzhong
# @FileName: HJ076.py
# @Software: PyCharm

n = int(input())
first = pow(n,2) - n + 1
outstr = ''
for i in range(n):
    outstr += str(first) + '+'
    first += 2
print(outstr[:-1])