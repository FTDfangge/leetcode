# -*- coding: utf-8 -*-
# @Time    : 2022-09-08 12:03 a.m.
# @Author  : qkzhong
# @FileName: HJ040.py
# @Software: PyCharm
s = input()
c = [0] * 4
for i in s:
    if i.isalpha():
        c[0] += 1
    elif i == ' ':
        c[1] += 1
    elif i.isdigit():
        c[2] += 1
    else:
        c[3] += 1
for i in c:
    print(i)