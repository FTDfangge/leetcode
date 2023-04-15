# -*- coding: utf-8 -*-
# @Time    : 2022-03-19 5:47 p.m.
# @Author  : qkzhong
# @FileName: 426_tree_to_doublylist.py
# @Software: PyCharm
class Node:
    def __init__(self, val, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def connect_to_subtree(current_node: Node, is_left: bool) -> Node:
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


if __name__ == '__main__':
    root = Node(8, Node(6, Node(2, Node(1), Node(4, Node(3), Node(5))), Node(7)), Node(12, Node(10, Node(9), Node(11)), Node(13)))
    out = Solution().treeToDoublyList(Node(2, Node(1)))
    while out:
        print(out.val)
        out = out.right
