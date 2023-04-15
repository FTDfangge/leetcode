# -*- coding: utf-8 -*-
# @Time    : 2022-09-15 7:48 p.m.
# @Author  : qkzhong
# @FileName: interviwe.py
# @Software: PyCharm

list = [0,0,1,0,0,3,12,0 ]

ptr1 = 0
ptr2 = 0

while ptr1 in range(list.__len__()):
    if list[ptr1] != 0:
        list[ptr2] = list[ptr1]
        ptr1 += 1
        ptr2 += 1
    else:
        ptr1 +=1

while ptr2 in range(list.__len__()):
    list[ptr2] = 0
    ptr2 += 1

print(list)