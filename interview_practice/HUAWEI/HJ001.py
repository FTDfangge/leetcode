# -*- coding: utf-8 -*-
# @Time    : 2022-09-03 11:35 p.m.
# @Author  : qkzhong
# @FileName: HJ001.py
# @Software: PyCharm

# 描述
# 计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
# 输入描述：
# 输入一行，代表要计算的字符串，非空，长度小于5000。
#
# 输出描述：
# 输出一个整数，表示输入字符串最后一个单词的长度。


str = input()
length = 0
for i in range(str.__len__() - 1, -1, -1):
    if str[i] == " ":
        break

    length += 1

print(length)