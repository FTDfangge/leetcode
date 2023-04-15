# -*- coding: utf-8 -*-
# @Time    : 2022-03-23 1:54 p.m.
# @Author  : qkzhong
# @FileName: 105_build_tree.py
# @Software: PyCharm

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        if preorder == inorder and preorder.__len__() == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index_of_root = 0
        while inorder[index_of_root] != preorder[0]:
            index_of_root += 1
        root.left = self.buildTree(preorder[1:index_of_root + 1], inorder[:index_of_root])
        root.right = self.buildTree(preorder[index_of_root + 1:], inorder[index_of_root + 1:])
        return root


if __name__ == '__main__':
    print(Solution().buildTree([1,2], [1, 2]))
