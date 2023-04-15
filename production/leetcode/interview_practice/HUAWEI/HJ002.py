# -*- coding: utf-8 -*-
# @Time    : 2022-09-03 11:40 p.m.
# @Author  : qkzhong
# @FileName: HJ002.py
# @Software: PyCharm

# 描述
# 写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）
#
# 数据范围： 1 \le num \le 1000 \1≤num≤1000
# 输入描述：
# 第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字符。
#
# 输出描述：
# 输出输入字符串中含有该字符的个数。（不区分大小写字母）

import sys
str = input().upper()
letter = input().upper()
number = 0
for i in str:
    if letter == i:
        number += 1
print(number)
