# -*- coding: utf-8 -*-
# @Time    : 2022-03-12 2:33 p.m.
# @Author  : qkzhong
# @FileName: jianzhi11_min_array.py
# @Software: PyCharm

# AC
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = numbers.__len__() - 1
        while left <= right:
            if numbers[left] < numbers[right]:
                return numbers[left]
            else:
                mid = int((left + right) / 2)
                if numbers[left] == numbers[mid] and numbers[mid] == numbers[right]:
                    m = numbers[left]
                    for i in range(left, right):
                        m = min(m, numbers[i])
                    return m
                else:
                    if numbers[mid] >= numbers[left]:
                        # in the right hand
                        left = mid + 1
                    else:
                        # in the left hand
                        right = mid
        return numbers[right]


if __name__ == '__main__':
    print(Solution().minArray([1,1]))
