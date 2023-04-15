# -*- coding: utf-8 -*-
# @Time    : 2022-09-04 3:45 p.m.
# @Author  : qkzhong
# @FileName: HJ008.py
# @Software: PyCharm

# 描述
# 数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。
#
#
# 提示:
# 0 <= index <= 11111111
# 1 <= value <= 100000
#
# 输入描述：
# 先输入键值对的个数n（1 <= num <= 500）
# 接下来n行每行输入成对的index和value值，以空格隔开
#
# 输出描述：
# 输出合并后的键值对（多行）

mydict = {}
number = int(input())
for i in range(number):
    key, value = input().split(" ")
    key = int(key)
    value = int(value)
    if key in mydict:
        mydict[key] += value
    else:
        mydict[key] = value


def sortedDict(adict):
    keys = list(adict.keys())

    keys.sort()

    return keys, [adict[key] for key in keys]


sortedkeys, sortedvals = sortedDict(mydict)
for i in range(mydict.__len__()):
    print(sortedkeys[i], sortedvals[i])