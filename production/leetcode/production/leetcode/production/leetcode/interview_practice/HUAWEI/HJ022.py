# -*- coding: utf-8 -*-
# @Time    : 2022-09-06 10:55 p.m.
# @Author  : qkzhong
# @FileName: HJ022.py
# @Software: PyCharm

import sys

for line in sys.stdin:
    if line.rstrip("\n") == '0':
        break
    n = int(line)
    drink = 0
    while n // 3 > 0:
        drink += n // 3
        n = n // 3 + n % 3
    if n == 2:
        drink += 1
    print(drink)
