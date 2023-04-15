# -*- coding: utf-8 -*-
# @Time    : 2021-06-04 10:17 a.m.
# @Author  : qkzhong
# @FileName: 88_merge.py
# @Software: PyCharm

# AC(leetcode神经病，nums1已经是[1]了，硬要告诉我结果是[0]，返回值不对)

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        elif m == 0:
            nums1 = nums2
        else:
            i1 = m - 1
            i2 = n - 1
            back_ptr = m + n - 1
            while (i1 in range(m)) and (i2 in range(n)):
                if nums1[i1] < nums2[i2]:
                    nums1[back_ptr] = nums2[i2]
                    i2 -= 1
                else:
                    nums1[back_ptr] = nums1[i1]
                    i1 -= 1
                back_ptr -= 1
        print(nums1)


if __name__ == '__main__':
    Solution().merge([0], 0, [1], 1)
