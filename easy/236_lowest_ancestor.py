# -*- coding: utf-8 -*-
# @Time    : 2022-03-21 4:02 p.m.
# @Author  : qkzhong
# @FileName: 236_lowest_ancestor.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.table = {}
        self.depth = 0

    def isAncestor(self,  root: TreeNode, t: TreeNode) -> bool:
        if not root:
            return False
        if root == t:
            return True
        if root.left == t or root.right == t:
            return True
        return self.isAncestor(root.left, t) or self.isAncestor(root.right, t)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if self.isAncestor(root.left, p) and self.isAncestor(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        elif self.isAncestor(root.right, p) and self.isAncestor(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(5)
    tree.right = TreeNode(1)
    tree.left.left = TreeNode(6)
    tree.left.right = TreeNode(2)
    tree.right.left = TreeNode(0)
    tree.right.right = TreeNode(8)
    tree.left.right.left = TreeNode(7)
    tree.left.right.right = TreeNode(4)
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.left.right.right))