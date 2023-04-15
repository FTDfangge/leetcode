# -*- coding: utf-8 -*-
# @Time    : 2022-03-20 3:47 p.m.
# @Author  : qkzhong
# @FileName: jianzhi55_I_tree_depth.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    # root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)
    # root.right.left.right = TreeNode(4)
    print(Solution().maxDepth(root))
