# -*- coding: utf-8 -*-
# @Time    : 2022-03-18 7:32 p.m.
# @Author  : qkzhong
# @FileName: jianzhi34_path_sum.py
# @Software: PyCharm
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.path = []
        self.output = []

    # this solution could solve all path that start at root, end must be leaf
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        self.path = []
        self.output = []

        def dfs(start_node: TreeNode):
            if not start_node:
                # this path is invalid
                return False
            if not start_node.right and not start_node.left: # leaf
                self.path.append(start_node.val)
                # check if the path is valid
                if sum(self.path) == target:
                    self.output.append(self.path[:])
                    self.path.pop()
                    return True
                else:
                    self.path.pop()
                    return False
            else:
                self.path.append(start_node.val)
                l = dfs(start_node.left)
                r = dfs(start_node.right)

                if l or r:
                    self.path.pop()
                    return True
                self.path.pop()
                return False
        print(dfs(root))
        return self.output

    # this solution could solve all path that start at root, end could be any node
    def pathSum2(self, root: TreeNode, target: int) -> List[List[int]]:
        self.path = []

        def dfs(start_node: TreeNode, tar: int):
            if not start_node and tar == 0:
                return True
            if not start_node:
                # this path is invalid
                return False

            if start_node.val == tar:
                # correct path and meet the end
                self.path.append(start_node.val)
                self.output.append(self.path[:])
                self.path.pop()
                return True
            elif start_node.left or start_node.right:
                self.path.append(start_node.val)
                l = dfs(start_node.left, tar - start_node.val)
                r = dfs(start_node.right, tar - start_node.val)
                if l or r:
                    self.path.pop()
                    return True

                return False
            else:
                return False

        if dfs(root, target):
            return self.output
        else:
            return []


if __name__ == '__main__':
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    root2 = TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))
    print(Solution().pathSum(root2, 2))
