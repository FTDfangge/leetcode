from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if root1 and not root2:
            return root1
        if not root1 and root2:
            return root2

        new_tree = TreeNode()
        if root1:
            new_tree.val += root1.val
        if root2:
            new_tree.val += root2.val

        if root1.left and root2.left:
            new_tree.left = self.mergeTrees(root1.left, root2.left)
        elif root1.left:
            new_tree.left = root1.left
        elif root2.left:
            new_tree.left = root2.left

        if root1.right and root2.right:
            new_tree.right = self.mergeTrees(root1.right, root2.right)
        elif root1.right:
            new_tree.right = root1.right
        elif root2.right:
            new_tree.right = root2.right
        return new_tree
