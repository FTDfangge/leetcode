# -*- coding: utf-8 -*-
# @Time    : 2022-03-19 5:48 p.m.
# @Author  : qkzhong
# @FileName: jianzhi54_kth_largest.py
# @Software: PyCharm
from typing import List


class TreeNode:
    def __init__(self, val, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.list = []
    def treeToDoublyList(self, root: 'TreeNode') -> 'TreeNode':
        def connect_to_subtree(current_node: TreeNode, is_left: bool) -> TreeNode:
            if not current_node:
                return None
            if not current_node.left and not current_node.right:
                return current_node
            else:
                l = connect_to_subtree(current_node.left, True)
                r = connect_to_subtree(current_node.right, False)
                if l:
                    l.right = current_node
                    current_node.left = l
                if r:
                    r.left = current_node
                    current_node.right = r
                ptr = current_node
            if is_left:
                while ptr.right:
                    ptr = ptr.right
                return ptr
            else:
                while ptr.left:
                    ptr = ptr.left
                return ptr
        if root:
            head = connect_to_subtree(root, False)

            ptr2= root
            while ptr2.right:
                ptr2 = ptr2.right
            head.left = ptr2
            ptr2.right = head
            return head
        else:
            return None

    def kthLargest(self, root: TreeNode, k: int) -> int:
        node = self.treeToDoublyList(root)
        for i in range(k):
            node = node.left
        return node.val

    def kthLargest2(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res



if __name__ == '__main__':
    root = TreeNode(8, TreeNode(6, TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(7)), TreeNode(12, TreeNode(10, TreeNode(9), TreeNode(11)), TreeNode(13)))
    print(Solution().kthLargest2(root, 3))