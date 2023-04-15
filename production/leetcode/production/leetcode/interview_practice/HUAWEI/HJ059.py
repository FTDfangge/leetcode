# -*- coding: utf-8 -*-
# @Time    : 2022-09-08 12:08 a.m.
# @Author  : qkzhong
# @FileName: HJ059.py
# @Software: PyCharm

s = input()
char_dict = {}
for i in s:
    if i in char_dict:
        char_dict[i] += 1
    else:
        char_dict[i] = 1
exist = False
for i in char_dict:
    if char_dict[i] == 1:
        print(i)
        exist = True
        break
if not exist:
    print(-1)