# -*- coding: utf-8 -*-
# @Time    : 2022-03-12 5:47 p.m.
# @Author  : qkzhong
# @FileName: jianzhi32_III_level_order_bintree.py
# @Software: PyCharm

# AC
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

        current_stack = 0
        next_stack = 1
        output = []
        level = []
        stack = [[], []]
        node = root
        stack[current_stack].append(node)
        while (stack[current_stack] != []) or (stack[next_stack] != []) :
            node = stack[current_stack].pop()
            level.append(node.val)
            if current_stack == 0:
                if node.left:
                    stack[next_stack].append(node.left)
                if node.right:
                    stack[next_stack].append(node.right)
            elif current_stack == 1:
                if node.right:
                    stack[next_stack].append(node.right)
                if node.left:
                    stack[next_stack].append(node.left)

            if not stack[current_stack]:
                output.append(level)
                level = []
                current_stack = 1 - current_stack
                next_stack = 1 - next_stack

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
