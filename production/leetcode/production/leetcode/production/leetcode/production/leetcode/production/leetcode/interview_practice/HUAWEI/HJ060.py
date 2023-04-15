# -*- coding: utf-8 -*-
# @Time    : 2022-09-07 11:54 p.m.
# @Author  : qkzhong
# @FileName: HJ060.py
# @Software: PyCharm
import math


def check_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
for i in range(n//2):
    if check_prime(n//2 - i) and check_prime(n//2 + i):
        print(n//2 - i)
        print(n//2 + i)
        break