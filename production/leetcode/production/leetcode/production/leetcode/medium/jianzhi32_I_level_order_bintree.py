# -*- coding: utf-8 -*-
# @Time    : 2022-03-12 4:45 p.m.
# @Author  : qkzhong
# @FileName: jianzhi32_I_level_order_bintree.py
# @Software: PyCharm
import collections
from queue import Queue
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        output = []
        q = collections.deque()
        node = root
        q.append(node)
        while q:
            node = q.popleft()
            output.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return output
