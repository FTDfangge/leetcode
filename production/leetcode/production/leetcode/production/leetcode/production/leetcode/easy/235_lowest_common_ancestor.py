# -*- coding: utf-8 -*-
# @Time    : 2022-03-21 3:17 p.m.
# @Author  : qkzhong
# @FileName: 235_lowest_common_ancestor.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


if __name__ == '__main__':
    tree = TreeNode(6)
    tree.left = TreeNode(2)
    tree.right = TreeNode(8)
    tree.left.left = TreeNode(0)
    tree.left.right = TreeNode(4)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(9)
    tree.left.right.left = TreeNode(3)
    tree.left.right.right = TreeNode(5)
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.left.right))
