# -*- coding: utf-8 -*-
# @Time    : 2022-11-19 1:42 p.m.
# @Author  : qkzhong
# @FileName: 166_fraction2decimal.py
# @Software: PyCharm
def get_repeat_len(n, m) -> int:
    s = ''
    target = n
    while True:
        while n // m == 0:
            n *= 10
            s += '0'
        s = s[:-1]
        s += str(n // m)
        n = n % m
        if n == target:
            return s.__len__()


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        is_negative = False
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            is_negative = True
        numerator = abs(numerator)
        denominator = abs(denominator)
        dec_str = '.'
        integer = numerator // denominator
        numerator = numerator % denominator
        if numerator == 0:
            if is_negative:
                return '-' + str(integer)
            return str(integer)
        d_set = [numerator]
        while numerator != 0:
            while numerator // denominator == 0:
                dec_str += '0'
                numerator *= 10
            dec_str = dec_str[:-1]
            dec_str += str(numerator // denominator)
            numerator = numerator % denominator
            if numerator in d_set:  # 循环小数
                repeat_len = get_repeat_len(numerator, denominator)
                repeat = dec_str[-repeat_len:]
                dec_str = dec_str[:-repeat_len]
                if is_negative:
                    return '-' + str(integer) + dec_str + '(' + str(repeat) + ')'
                return str(integer) + dec_str + '(' + str(repeat) + ')'
            else:
                d_set.append(numerator)
        if is_negative:
            return '-' + str(integer) + dec_str
        return str(integer) + dec_str


print(Solution().fractionToDecimal(-2147483648
,1))
