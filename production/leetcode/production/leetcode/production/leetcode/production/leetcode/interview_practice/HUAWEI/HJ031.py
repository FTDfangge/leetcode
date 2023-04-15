# -*- coding: utf-8 -*-
# @Time    : 2022-09-10 4:16 p.m.
# @Author  : qkzhong
# @FileName: HJ031.py
# @Software: PyCharm

s = input()
word_list = []
i = j = 0

while i < s.__len__() and j < s.__len__():
    if s[j].isalpha():
        j += 1
    else:
        word_list.append(s[i:j])
        j += 1
        i = j
word_list.append(s[i:j])

word_list = word_list[::-1]
out = ''
for w in word_list:
    out += w + ' '
out = out.rstrip(' ')
print(out)

