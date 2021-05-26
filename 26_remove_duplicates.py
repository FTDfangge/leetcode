# -*- coding: utf-8 -*-
# @Time    : 2021-05-25 10:47 a.m.
# @Author  : qkzhong
# @FileName: 26_remove_duplicates.py
# @Software: PyCharm

# AC

from typing import List


class Solution:
    def removeDuplicates(nums: List[int]) -> int:
        if not nums:
            return 0

        fast = slow = 1
        while fast < nums.__len__():
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


if __name__ == '__main__':
    print(Solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
