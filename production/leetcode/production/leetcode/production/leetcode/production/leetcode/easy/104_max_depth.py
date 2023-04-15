# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 5:28 p.m.
# @Author  : qkzhong
# @FileName: 104_max_depth.py
# @Software: PyCharm

# AC
class TreeNode:
    __slots__ = ('val', 'left', 'right')

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        else:
            return 0


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

if __name__ == '__main__':
    root = stringToTreeNode('[3,9,20,null,null,15,7]')
    print(Solution().maxDepth(root))


