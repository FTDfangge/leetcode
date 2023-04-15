from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_Tree(node: TreeNode, val: int) -> bool:
    if not node:
        return True
    if node.val != val:
        return False
    else:
        return check_Tree(node.left, val) and check_Tree(node.right, val)


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        if check_Tree(root, target):
            return None
        q = [root]
        while q:
            cur = q.pop(0)
            if check_Tree(cur.left, target):
                cur.left = None
            else:
                q.append(cur.left)
            if check_Tree(cur.right, target):
                cur.right = None
            else:
                q.append(cur.right)
        return root