# -*- coding: utf-8 -*-
# @Time    : 2022-03-12 5:15 p.m.
# @Author  : qkzhong
# @FileName: jianzhi32_II_level_order_bintree.py
# @Software: PyCharm
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        output = []
        level_out = []
        this_level = 1
        next_level = 0
        q = collections.deque()
        node = root
        q.append(node)

        while q:
            node = q.popleft()
            this_level -= 1
            level_out.append(node.val)

            if node.left:
                q.append(node.left)
                next_level += 1
            if node.right:
                q.append(node.right)
                next_level += 1

            if this_level == 0:
                this_level = next_level
                next_level = 0
                output.append(level_out)
                level_out = []

        return output


if __name__ == '__main__':
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.right = TreeNode('c')
    root.left.left = TreeNode('d')
    root.left.right = TreeNode('e')
    root.right.left = TreeNode('f')
    root.right.left.left = TreeNode('g')
    root.right.left.right = TreeNode('h')
    print(Solution().levelOrder(root))
