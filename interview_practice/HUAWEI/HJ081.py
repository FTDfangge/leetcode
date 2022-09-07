# -*- coding: utf-8 -*-
# @Time    : 2022-09-08 12:26 a.m.
# @Author  : qkzhong
# @FileName: HJ081.py
# @Software: PyCharm
import sys

short = input()
long = input()
short_dict = {}

for i in short:
    if i not in short_dict:
        short_dict[i] = 0

for i in long:
    if i in short_dict:
        short_dict[i] = 1

for i in short_dict:
    if not short_dict[i]:
        print('false')
        sys.exit(0)

print('true')