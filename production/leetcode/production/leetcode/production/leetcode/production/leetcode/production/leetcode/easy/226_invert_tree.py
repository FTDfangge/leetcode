# -*- coding: utf-8 -*-
# @Time    : 2022-03-14 4:10 p.m.
# @Author  : qkzhong
# @FileName: 226_invert_tree.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        node = TreeNode(root.val)
        node.left = self.invertTree(root.right)
        node.right = self.invertTree(root.left)

        return node