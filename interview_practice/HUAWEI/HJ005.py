# -*- coding: utf-8 -*-
# @Time    : 2022-09-04 1:02 p.m.
# @Author  : qkzhong
# @FileName: HJ005.py
# @Software: PyCharm

# 描述
# 写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
#
# 数据范围：保证结果在 1 \le num \le 2^{31}-1 \1≤num≤2
# 31
#  −1
# 输入描述：
# 输入一个十六进制的数值字符串。
#
# 输出描述：
# 输出该数值的十进制字符串。不同组的测试用例用\n隔开。

str = input()[2:]
hexdict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
num = 0
exponent = 0
for i in range(str.__len__() -1, -1, -1):
    num += hexdict[str[i]] * pow(16,exponent)
    exponent += 1
print(num)