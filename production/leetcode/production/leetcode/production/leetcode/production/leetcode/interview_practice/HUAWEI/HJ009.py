# -*- coding: utf-8 -*-
# @Time    : 2022-09-04 4:00 p.m.
# @Author  : qkzhong
# @FileName: HJ009.py
# @Software: PyCharm

# 描述
# 输入一个
# int
# 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
# 保证输入的整数最后一位不是
# 0 。
#
# 数据范围： 1 \le
# num \le
# 10 ^ {8} \1≤num≤10
# 8
#
# 输入描述：
# 输入一个int型整数
#
# 输出描述：
# 按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

n = int(input())
s = set()
outstr = ""
while n > 0:
    if n % 10 not in s:
        outstr += str(n % 10)
        s.add(n % 10)
    n = n // 10
print(outstr)