# -*- coding: utf-8 -*-
# @Time    : 2022-09-10 3:57 p.m.
# @Author  : qkzhong
# @FileName: HJ023.py
# @Software: PyCharm

s = input()
my_min = 20
out = ''

s_dict = {}
for i in s:
    if i in s_dict:
        s_dict[i] += 1
    else:
        s_dict[i] = 1

for i in s_dict:
    my_min = min(s_dict[i], my_min)

for i in s_dict.copy():
    if s_dict[i] == my_min:
        s_dict.__delitem__(i)

for i in s:
    if i in s_dict:
        out+=i

print(out)