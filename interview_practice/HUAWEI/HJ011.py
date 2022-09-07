# -*- coding: utf-8 -*-
# @Time    : 2022-09-04 7:08 p.m.
# @Author  : qkzhong
# @FileName: HJ011.py
# @Software: PyCharm

# 描述
# 输入一个整数，将这个整数以字符串的形式逆序输出
# 程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001
#
#
# 数据范围： 0 \le num \le 2^{30}-1 \0≤num≤2
# 30
#  −1
# 输入描述：
# 输入一个int整数
#
# 输出描述：
# 将这个整数以字符串的形式逆序输出

n = int(input())
if n == 0:
    print(0)
outstr = ""
while n > 0:
    outstr += str(n % 10)
    n //= 10
print(outstr)