# -*- coding: utf-8 -*-
# @Time    : 2022-09-05 8:33 p.m.
# @Author  : qkzhong
# @FileName: HJ018.py
# @Software: PyCharm

# 描述
# 请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。
#
# 所有的IP地址划分为 A,B,C,D,E五类
#
# A类地址从1.0.0.0到126.255.255.255;
#
# B类地址从128.0.0.0到191.255.255.255;
#
# C类地址从192.0.0.0到223.255.255.255;
#
# D类地址从224.0.0.0到239.255.255.255；
#
# E类地址从240.0.0.0到255.255.255.255
#
#
# 私网IP范围是：
#
# 从10.0.0.0到10.255.255.255
#
# 从172.16.0.0到172.31.255.255
#
# 从192.168.0.0到192.168.255.255
#
#
# 子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
# （注意二进制下全是1或者全是0均为非法子网掩码）
#
# 注意：
# 1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略
# 2. 私有IP地址和A,B,C,D,E类地址是不冲突的
#
# 输入描述：
# 多行字符串。每行一个IP地址和掩码，用~隔开。
#
# 请参考帖子https://www.nowcoder.com/discuss/276处理循环输入的问题。
# 输出描述：
# 统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。

import sys

A = 0
B = 0
C = 0
D = 0
E = 0
wrong = 0
private = 0
valid_mask = [0, 128, 192, 224, 240, 248, 252, 254, 255]


def get_ip_type(ip: str) -> str:
    sections = ip.split(".")
    if sections.__len__() != 4:
        return "F"
    if int(sections[0]) == 0 or int(sections[0]) == 127:
        return "I"
    for s in sections:
        if s.__len__() <= 0:
            return "F"
        if int(s) > 255 or int(s) < 0:
            return "F"
    # 这是一个合理的IP地址
    if int(sections[0]) >= 1 and int(sections[0]) <= 126:
        if int(sections[0]) == 10:
            return "Ap"
        return "A"
    elif int(sections[0]) >= 128 and int(sections[0]) <= 191:
        if int(sections[0]) == 172 and int(sections[1]) >= 16 and int(sections[1]) <= 31:
            return "Bp"
        return "B"
    elif int(sections[0]) >= 192 and int(sections[0]) <= 223:
        if int(sections[0]) == 192 and int(sections[1]) == 168:
            return "Cp"
        return "C"
    elif int(sections[0]) >= 224 and int(sections[0]) <= 239:
        return "D"
    elif int(sections[0]) >= 240 and int(sections[0]) <= 255:
        return "E"

    return ""


def is_mask_valid(mask: str) -> bool:
    if mask == "255.255.255.255" or mask == "0.0.0.0":
        return False

    sections = mask.split(".")
    if sections.__len__() != 4:
        return False
    have_zero = False
    for s in sections:
        if s.__len__() <= 0:
            return False
        if not have_zero:
            if int(s) != 255:
                have_zero = True
                if not int(s) in valid_mask:
                    return False
            continue
        if int(s) != 0:
            return False
    return True


for line in sys.stdin:
    ip, mask = line.split("~")
    mask = mask.rstrip("\n")
    ip_type = get_ip_type(ip)
    mask_valid = is_mask_valid(mask)
    if ip_type == "I":
        continue
    if (ip_type == "A" or ip_type == "Ap") and mask_valid:
        A += 1
        #         print("A")
        if ip_type == "Ap":
            private += 1
    #             print("Ap")
    elif (ip_type == "B" or ip_type == "Bp") and mask_valid:
        B += 1
        #         print("B")
        if ip_type == "Bp":
            private += 1
    #             print("Bp")
    elif (ip_type == "C" or ip_type == "Cp") and mask_valid:
        C += 1
        #         print("C")
        if ip_type == "Cp":
            private += 1
    #             print("Cp")
    elif ip_type == "D" and mask_valid:
        D += 1
    #         print("D")
    elif ip_type == "E" and mask_valid:
        E += 1
    #         print("E")
    elif ip_type == "F":
        wrong += 1
    #         print("w")
    elif not mask_valid:
        wrong += 1
#         print("w")

print(A, B, C, D, E, wrong, private)