# -*- coding: utf-8 -*-
# @Time    : 2021-06-03 3:31 p.m.
# @Author  : qkzhong
# @FileName: 102_level_order.py
# @Software: PyCharm


# AC

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Level_tree:
    def __init__(self, val=0, left=None, right=None, level=-1):
        self.val = val
        self.left = left
        self.right = right
        self.level = level


def generate_levelTree_from_tree(tree: TreeNode, level) -> Level_tree:
    levelTree = Level_tree()
    if tree:
        levelTree.val = tree.val
        levelTree.level = level
        levelTree.left = generate_levelTree_from_tree(tree.left, level + 1)
        levelTree.right = generate_levelTree_from_tree(tree.right, level + 1)
        return levelTree
    else:
        return None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        level_tree = generate_levelTree_from_tree(root, 0)
        if not root:
            return []
        queue = [level_tree]
        current_level = -1
        levelOrder_list = []
        while queue:
            current_node = queue.pop(0)
            if current_node.level != current_level:
                levelOrder_list.append([])
                current_level = current_node.level
            levelOrder_list[levelOrder_list.__len__()-1].append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return levelOrder_list


if __name__ == '__main__':
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().levelOrder(tree))
