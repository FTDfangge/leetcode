# -*- coding: utf-8 -*-
# @Time    : 2022-09-04 9:08 p.m.
# @Author  : qkzhong
# @FileName: HJ014.py
# @Software: PyCharm


# 描述
# 给定 num 个字符串，请对 num 个字符串按照字典序排列。
#
# 数据范围： 1 \le num \le 1000 \1≤num≤1000  ，字符串长度满足 1 \le len \le 100 \1≤len≤100
# 输入描述：
# 输入第一行为一个正整数n(1≤num≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
# 输出描述：
# 数据输出n行，输出结果为按照字典序排列的字符串。

n = int(input())
array = []
for i in range(n):
    array.append(input())

for i in range(n - 1):
    for j in range (n - i - 1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
for i in array:
    print(i)