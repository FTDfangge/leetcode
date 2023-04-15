# -*- coding: utf-8 -*-
# @Time    : 2022-03-14 4:13 p.m.
# @Author  : qkzhong
# @FileName: jianzhi28_is_symmetric_tree.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def check_symmetric(self, A: TreeNode, B: TreeNode) -> bool:
        if (not A) and (not B):
            return True
        elif A and B and A.val == B.val:
            return self.check_symmetric(A.left, B.right) and self.check_symmetric(A.right, B.left)
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is not None:
            return self.check_symmetric(root.left, root.right)
        else:
            return True