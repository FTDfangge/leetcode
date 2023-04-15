# -*- coding: utf-8 -*-
# @Time    : 2022-09-04 1:35 p.m.
# @Author  : qkzhong
# @FileName: HJ006.py
# @Software: PyCharm

# 描述
# 功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
#
#
# 数据范围： 1 \le num \le 2 \times 10^{9} + 14 \1≤num≤2×10
# 9
#  +14
# 输入描述：
# 输入一个整数
#
# 输出描述：
# 按照从小到大的顺序输出它的所有质数的因子，以空格隔开。

import math

integer = int(input())
factor = 2
while(factor <= int(math.sqrt(integer)) + 1):
    while (integer % factor == 0):
        integer = integer // factor
        print(factor, end= " ")
    factor += 1
if integer > 2:
    print(integer)