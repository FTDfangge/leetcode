# -*- coding: utf-8 -*-
# @Time    : 2022-09-04 7:48 p.m.
# @Author  : qkzhong
# @FileName: HJ013.py
# @Software: PyCharm

# 描述
# 将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
#
# 所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
#
# 数据范围：输入的字符串长度满足 1 \le num \le 1000 \1≤num≤1000
#
# 注意本题有多组输入
# 输入描述：
# 输入一个英文语句，每个单词用空格隔开。保证输入只包含空格和字母。
#
# 输出描述：
# 得到逆序的句子

mystr = input()
mystr = mystr[::-1]
head_ptr = 0
outstr = ""
for i in range(mystr.__len__()):
    if mystr[i] == " ":
        outstr += mystr[head_ptr:i][::-1]
        outstr += " "
        head_ptr = i + 1
outstr += mystr[head_ptr:][::-1]
print(outstr)
