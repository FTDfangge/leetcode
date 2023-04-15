# -*- coding: utf-8 -*-
# @Time    : 2022-09-04 9:25 p.m.
# @Author  : qkzhong
# @FileName: HJ015.py
# @Software: PyCharm

# 描述
# 输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。
#
# 数据范围：保证在 32 位整型数字范围内
# 输入描述：
#  输入一个整数（int类型）
#
# 输出描述：
#  这个数转换成2进制后，输出1的个数

n = int(input())
zero_num = 0
while n > 0:
    if n % 2:
        zero_num += 1
    n //= 2
print(zero_num)