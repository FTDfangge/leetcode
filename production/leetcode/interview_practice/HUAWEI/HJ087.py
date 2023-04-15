# -*- coding: utf-8 -*-
# @Time    : 2022-09-07 11:33 p.m.
# @Author  : qkzhong
# @FileName: HJ087.py
# @Software: PyCharm

s = input()
score = 0
check = [0]*4 # 分别对应是否有 大写字母，小写字母，数字，符号

# 密码长度加分
length = s.__len__()
if length <= 4:
    score += 5
elif length <=7:
    score += 10
else:
    score += 25

for i in s:
    if i.isupper():
        check[0] = 1
    elif i.islower():
        check[1] = 1
    elif i.isdigit():
        check[2] += 1
    else:
        check[3] += 1
    if check == [1, 1, 2, 2]:
        break

# 字母加分
if check[0] and check[1]:
    score += 20
elif check[0] or check[1]:
    score += 10

# 数字加分
if check[2] == 1:
    score += 10
if check[2] >= 2:
    score += 20

# 符号加分
if check[3] == 1:
    score += 10
if check[3] >= 2:
    score += 25

# 奖励加分
if (check[0] and check[1]) and check[2] and check[3]:
    score += 5
elif (check[0] or check[1]) and check[2] and check[3]:
    score += 3
elif (check[0] or check[1]) and check[2]:
    score += 2

if score >= 90:
    print('VERY_SECURE')
elif score >= 80:
    print('SECURE')
elif score >= 70:
    print('VERY_STRONG')
elif score >= 60:
    print('STRONG')
elif score >= 50:
    print('AVERAGE')
elif score >= 25:
    print('WEAK')
else:
    print('VERY_WEAK')