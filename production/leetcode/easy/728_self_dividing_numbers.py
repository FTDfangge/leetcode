# -*- coding: utf-8 -*-
# @Time    : 2022-03-31 1:44 p.m.
# @Author  : qkzhong
# @FileName: 728_self_dividing_numbers.py
# @Software: PyCharm
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing_number(num : int):
            string = str(num)
            for s in string:
                if int(s) == 0:
                    return False
                if num % int(s) != 0:
                    return False
            return True

        res = []
        for n in range(left, right+1):
            if is_self_dividing_number(n):
                res.append(n)
        return res
