# -*- coding: utf-8 -*-
# @Time    : 2021-11-0810:01 p.m.
# @Author  : raynor
# @FileName: 13_roman_to_int.py
# @Software: PyCharm

def symbol_to_value(symbol):
    if symbol == "I":
        return 1
    elif symbol == "V":
        return 5
    elif symbol == "X":
        return 10
    elif symbol == "L":
        return 50
    elif symbol == "C":
        return 100
    elif symbol == "D":
        return 500
    elif symbol == "M":
        return 1000


class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        for i in range(s.__len__()):
            integer += symbol_to_value(s[i])
            if i + 1 < s.__len__():
                if symbol_to_value(s[i]) < symbol_to_value(s[i + 1]):
                    integer -= 2 * symbol_to_value(s[i])
        return integer


if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))
