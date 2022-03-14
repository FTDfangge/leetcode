# -*- coding: utf-8 -*-
# @Time    : 2022-03-14 4:03 p.m.
# @Author  : qkzhong
# @FileName: jianzhi27_mirror_tree.py
# @Software: PyCharm

# AC

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        node = TreeNode(root.val)
        node.left = self.mirrorTree(root.right)
        node.right = self.mirrorTree(root.left)

        return node
