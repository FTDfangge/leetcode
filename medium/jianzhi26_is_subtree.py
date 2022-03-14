# -*- coding: utf-8 -*-
# @Time    : 2022-03-14 3:09 p.m.
# @Author  : qkzhong
# @FileName: jianzhi26_is_subtree.py
# @Software: PyCharm
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_included(self, A: TreeNode, B: TreeNode):
        if B is None:
            return True
        if A is None:
            return False
        if A.val == B.val:
            return self.is_included(A.left, B.left) and self.is_included(A.right, B.right)
        else:
            return False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None:
            return False
        if B is None:
            return False

        if A.val != B.val:
            return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        else:
            if self.is_included(A, B):
                return True
            else:
                return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    # root.left.right = TreeNode(2)
    # root.left.right.left = TreeNode(4)
    # root.left.right.right = TreeNode(7)

    sub = TreeNode(4)
    sub.left = TreeNode(1)
    # sub.right = TreeNode(2)

    print(Solution().isSubStructure(root, sub))
