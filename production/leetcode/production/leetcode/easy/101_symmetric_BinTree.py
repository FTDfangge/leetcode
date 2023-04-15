# -*- coding: utf-8 -*-
# @Time    : 2021-06-03 2:52 p.m.
# @Author  : qkzhong
# @FileName: 101_symmetric_BinTree.py
# @Software: PyCharm
from typing import List


# AC

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric_check(l: TreeNode, r: TreeNode):
            if (not l) and (not r):
                return True
            elif l and r:
                return l.val == r.val and symmetric_check(l.left, r.right) and symmetric_check(l.right, r.left)
            else:
                return False

        return symmetric_check(root, root)


if __name__ == '__main__':
    print(Solution().isSymmetric(TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(2, TreeNode(2)))))
