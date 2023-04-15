# -*- coding: utf-8 -*-
# @Time    : 2022-09-07 11:05 p.m.
# @Author  : qkzhong
# @FileName: HJ086.py
# @Software: PyCharm

n = int(input())
count = 0
m = 0
while n > 0:
    while n % 2 == 1:
        count += 1
        n //= 2
    m = max(m, count)
    n //= 2
    count = 0

print(m)

