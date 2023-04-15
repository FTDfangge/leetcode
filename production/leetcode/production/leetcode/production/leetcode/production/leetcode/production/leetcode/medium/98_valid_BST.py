# -*- coding: utf-8 -*-
# @Time    : 2021-06-03 1:50 p.m.
# @Author  : qkzhong
# @FileName: 98_valid_BST.py
# @Software: PyCharm


# AC
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_sub_valid(tree: TreeNode, lower_bound=float('-inf'), upperbound=float('inf')):
            if lower_bound < tree.val < upperbound:
                if (not tree.left) and (not tree.right):
                    return True
                left_valid = False
                right_valid = False
                if tree.left:
                    if tree.val <= tree.left.val:
                        return False
                    else:
                        left_valid = is_sub_valid(tree.left, lower_bound=lower_bound, upperbound=tree.val)
                else:
                    left_valid = True
                if tree.right:
                    if tree.val >= tree.right.val:
                        return False
                    else:
                        right_valid = is_sub_valid(tree.right, lower_bound=tree.val, upperbound=upperbound)
                else:
                    right_valid = True

                return left_valid and right_valid
            else:
                return False

        return is_sub_valid(root)


if __name__ == '__main__':
    node = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    print(Solution().isValidBST(node))
