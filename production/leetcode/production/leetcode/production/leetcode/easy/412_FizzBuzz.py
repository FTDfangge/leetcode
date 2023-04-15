# -*- coding: utf-8 -*-
# @Time    : 2021-11-088:41 p.m.
# @Author  : raynor
# @FileName: 412_FizzBuzz.py
# @Software: PyCharm

#AC

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzBuzz = []
        for i in range(n):
            if (i+1) % 15 == 0:
                fizzBuzz.append("FizzBuzz")
            elif (i+1) % 5 == 0:
                fizzBuzz.append("Buzz")
            elif (i+1) % 3 == 0:
                fizzBuzz.append("Fizz")
            else:
                fizzBuzz.append(str(i+1))
        return fizzBuzz


if __name__ == '__main__':
    print(Solution().fizzBuzz(20))
