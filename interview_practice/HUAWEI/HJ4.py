# -*- coding: utf-8 -*-
# @Time    : 2022-09-04 12:20 p.m.
# @Author  : qkzhong
# @FileName: HJ4.py
# @Software: PyCharm

# 描述
# •输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；
#
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
# 输入描述：
# 连续输入字符串(每个字符串长度小于等于100)
#
# 输出描述：
# 依次输出所有分割后的长度为8的新字符串

str = input()
if str.__len__() % 8 :
    str += "0"*(8 - str.__len__() % 8)
for i in range((str.__len__() // 8)+1):
    print(str[i*8:i*8+8])
