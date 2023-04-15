# -*- coding: utf-8 -*-
# @Time    : 2022-09-11 12:34 a.m.
# @Author  : qkzhong
# @FileName: tree_op.py
# @Software: PyCharm

class TreeNode:
    __slots__ = 'val', 'left', 'right'
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def list_2_tree(values :list) -> TreeNode:
    if not values:
        return None

    front = 0
    index = 1
    root = TreeNode(values[0])
    nodeQueue = [root]
    while index < values.__len__():
        node = nodeQueue[front]
        front += 1

        item = values[index]
        index += 1
        if item:
            # 左子树
            node.left = TreeNode(item)
            nodeQueue.append(node.left)

        if index > values.__len__():
            break

        item = values[index]
        index += 1
        if item:
            # 右子树
            node.right = TreeNode(item)
            nodeQueue.append(node.right)
    return root

def tree_2_list(root: TreeNode) ->list:
    output = []
    if not root:
        return []
    l = [root]
    index = 0
    while index < l.__len__():
        node = l[index]
        index += 1
        if not node:
            output.append(None)
            continue
        l.append(node.left)
        l.append(node.right)
        output.append(node.val)
    return output


if __name__ == '__main__':
    print(tree_2_list(TreeNode(3,
                         TreeNode(9), TreeNode(20,
                                               TreeNode(15,
                                                        TreeNode(13), TreeNode(4))))))

    list_2_tree([3, 9, 20, None, None, 15, None, 13, 4])