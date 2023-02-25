class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not Node else []


class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        def get_dept(node: Node, depth=0) -> int:
            temp_depth = depth
            if node.children:
                for c in node.children:
                    temp_depth = max(temp_depth, get_dept(c, depth + 1))
            return temp_depth

        def get_diameter(node: Node) -> int:
            if not node.children:
                return 0
            depths = []
            for i in node.children:
                depths.append(get_dept(i, 1))
            depths.sort()
            if depths.__len__() == 1:
                return depths[0]
            else:
                return depths[-1] + depths[-2]

        dia = 0
        q = [root]
        while q:
            cur = q.pop(0)
            dia = max(dia, get_diameter(cur))
            for c in cur.children:
                q.append(c)
        return dia


tree1 = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(Solution().diameter(tree1) == 3)
tree2 = Node(1, [Node(2, [Node(3, [Node(5), Node(6)]), Node(4, [Node(7)])])])
print(Solution().diameter(tree2) == 4)
