# -*- coding: utf-8 -*-
# @Time    : 2022-09-04 1:55 p.m.
# @Author  : qkzhong
# @FileName: HJ007.py
# @Software: PyCharm

# 描述
# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。
#
# 数据范围：保证输入的数字在 32 位浮点数范围内
# 输入描述：
# 输入一个正浮点数值
#
# 输出描述：
# 输出该数值的近似整数值

n = float(input())
if int(n * 2) % 2 == 0:
    print(int(n))
else:
    print(int(n) + 1)