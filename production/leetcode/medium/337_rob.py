from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        rob_dict = {None: 0}
        not_dict = {None: 0}

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            rob_dict[node] = not_dict[node.left] + not_dict[node.right] + node.val
            not_dict[node] = max(rob_dict[node.left], not_dict[node.left]) + \
                             max(rob_dict[node.right], not_dict[node.right])

        dfs(root)
        return max(rob_dict[root], not_dict[root])
