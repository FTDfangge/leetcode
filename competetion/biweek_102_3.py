# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([[root, 0]])
        level_tree = dict()
        level_sum = dict()
        brother_val = dict()
        while q:
            current, level = q.popleft()
            if current.left:
                q.append([current.left, level + 1])

                # fill level tree
                try:
                    level_tree[level + 1].append([current.left, current])
                except KeyError:
                    level_tree[level + 1] = [[current.left, current]]

                # update level sum
                try:
                    level_sum[level + 1] += current.left.val
                except KeyError:
                    level_sum[level + 1] = current.left.val

                # update brother val
                try:
                    brother_val[current] += current.left.val
                except KeyError:
                    brother_val[current] = current.left.val

            if current.right:
                q.append([current.right, level + 1])

                # fill level tree
                try:
                    level_tree[level + 1].append([current.right, current])
                except KeyError:
                    level_tree[level + 1] = [[current.right, current]]

                # update level sum
                try:
                    level_sum[level + 1] += current.right.val
                except KeyError:
                    level_sum[level + 1] = current.right.val

                # update brother val
                try:
                    brother_val[current] += current.right.val
                except KeyError:
                    brother_val[current] = current.right.val

        root.val = 0
        for item in level_tree.items():
            ll, nodes = item
            s = level_sum[ll]
            for node, parent in nodes:
                node.val = s - brother_val[parent]

        return root


root = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(10)), TreeNode(9, right=TreeNode(7)))
root = Solution().replaceValueInTree(root)
print()
