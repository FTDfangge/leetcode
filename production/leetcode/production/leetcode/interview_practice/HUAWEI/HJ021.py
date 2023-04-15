# -*- coding: utf-8 -*-
# @Time    : 2022-09-06 10:23 p.m.
# @Author  : qkzhong
# @FileName: HJ021.py
# @Software: PyCharm

old = input()
new = ""
for i in old:
    if 'A' <= i < "Z":
        new += chr(ord(i) + 97 - 65 + 1)
    elif i == 'Z':
        new += 'a'
    elif 'a' <= i <= 'c':
        new += '2'
    elif 'd' <= i <= 'f':
        new += '3'
    elif 'g' <= i <= 'i':
        new += '4'
    elif 'j' <= i <= 'l':
        new += '5'
    elif 'm' <= i <= 'o':
        new += '6'
    elif 'p' <= i <= 's':
        new += '7'
    elif 't' <= i <= 'v':
        new += '8'
    elif 'w' <= i <= 'z':
        new += '9'
    else:
        new += i
print(new)