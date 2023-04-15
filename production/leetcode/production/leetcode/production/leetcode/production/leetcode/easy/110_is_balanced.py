# -*- coding: utf-8 -*-
# @Time    : 2022-03-20 4:19 p.m.
# @Author  : qkzhong
# @FileName: 110_is_balanced.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)