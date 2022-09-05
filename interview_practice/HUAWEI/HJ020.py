# -*- coding: utf-8 -*-
# @Time    : 2022-09-05 9:52 p.m.
# @Author  : qkzhong
# @FileName: HJ020.py
# @Software: PyCharm

import sys


for line in sys.stdin:
    is_ng = False
    password = line.rstrip("\n")
    if password.__len__() <= 8:
        print("NG")
        is_ng = True
        continue
    s = set()
    for i in password:
        if i >= "A" and i <= "Z":
            s.add("Upper")
            if s.__len__() >= 3:
                break
        elif i >= "a" and i <= "z":
            s.add("low")
            if s.__len__() >= 3:
                break
        elif i >= "0" and i <= "9":
            s.add("num")
            if s.__len__() >= 3:
                break
        else:
            s.add("other")
            if s.__len__() >= 3:
                break
    if s.__len__() < 3:
        print("NG")
        is_ng = True
        continue
    s = set()
    for i in range(password.__len__()):
        if password[i:i+3] not in s:
            s.add(password[i:i+3])
        else:
            print("NG")
            is_ng = True
            break
    if not is_ng:
        print("OK")