# -*- coding: utf-8 -*-
# @Time    : 2022-09-07 11:15 p.m.
# @Author  : qkzhong
# @FileName: HJ085.py
# @Software: PyCharm

origin = input()
length = origin.__len__()
rev = origin[::-1]
my_matrix = [[0]* length for _ in range(length)]
m = 0

for i in range(length):
    for j in range(length):
        if origin[i] == rev[j]: #开始向右下搜寻
            offset = 0
            while i + offset < length and j + offset < length:
                if origin[i+offset] == rev[j+offset]:
                    my_matrix[i+offset][j+offset] = offset+1
                    offset += 1
                else:
                    break
            if i+j+offset == length: #保证回文是相连的
                m = max(offset, m)
print(m)