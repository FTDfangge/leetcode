# -*- coding: utf-8 -*-
# @Time    : 2022-03-11 8:53 p.m.
# @Author  : qkzhong
# @FileName: jianzhi53_count_in_sorted.py
# @Software: PyCharm

# AC

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        start = False
        for e in nums:
            if target == e:
                start = True
                count += 1
            elif start:
                break
        return count


if __name__ == '__main__':
    print(Solution().search([5, 7, 7, 8, 8, 10], 8))
