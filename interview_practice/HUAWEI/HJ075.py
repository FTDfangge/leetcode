# -*- coding: utf-8 -*-
# @Time    : 2022-09-07 3:35 p.m.
# @Author  : qkzhong
# @FileName: HJ075.py
# @Software: PyCharm

str1 = input()
str2 = input()
my_matrix = [[0]* str1.__len__() for _ in range(str2.__len__())]
max_len = 0

for i in range(str2.__len__()):
    for j in range(str1.__len__()):
        if str2[i] == str1[j]:
            if my_matrix[i][j] == 0: # 开始斜向下查找
                offset = 0
                while i+offset < str2.__len__() and j+offset < str1.__len__():
                    if str2[i+offset] == str1[j+offset]:
                        my_matrix[i+offset][j+offset] = offset+1
                        offset += 1
                    else:
                        break
                max_len = max(max_len, offset)
print(max_len)