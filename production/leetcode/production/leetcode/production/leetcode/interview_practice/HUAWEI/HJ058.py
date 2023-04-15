# -*- coding: utf-8 -*-
# @Time    : 2022-09-08 12:18 a.m.
# @Author  : qkzhong
# @FileName: HJ058.py
# @Software: PyCharm
n, k = list(map(int, input().split(' ')))
l = list(map(int, input().split(' ')))

length = l.__len__()
for i in range(min(length - 1, k)):
    for j in range(length - 1, 0, -1):
        if l[j] < l[j-1]:
            temp = l[j]
            l[j] = l[j-1]
            l[j-1] = temp
    print(l[i], end=' ')