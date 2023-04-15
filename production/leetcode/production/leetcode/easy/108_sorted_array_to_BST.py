# -*- coding: utf-8 -*-
# @Time    : 2021-06-04 9:48 a.m.
# @Author  : qkzhong
# @FileName: 108_sorted_array_to_BST.py
# @Software: PyCharm

# AC

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        midPoint = nums.__len__() // 2
        return TreeNode(val=nums[midPoint],
                        left=self.sortedArrayToBST(nums[0: midPoint]),
                        right=self.sortedArrayToBST(nums[midPoint + 1:nums.__len__()]))


if __name__ == '__main__':
    tree = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
    print('finish')
