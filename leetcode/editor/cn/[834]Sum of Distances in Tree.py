# There is an undirected connected tree with n nodes labeled from 0 to n - 1 
# and n - 1 edges. 
# 
#  You are given the integer n and the array edges where edges[i] = [ai, bi] 
# indicates that there is an edge between nodes ai and bi in the tree. 
# 
#  Return an array answer of length n where answer[i] is the sum of the 
# distances between the iᵗʰ node in the tree and all other nodes. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.
#  
# 
#  Example 2: 
#  
#  
# Input: n = 1, edges = []
# Output: [0]
#  
# 
#  Example 3: 
#  
#  
# Input: n = 2, edges = [[1,0]]
# Output: [1,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 3 * 10⁴ 
#  edges.length == n - 1 
#  edges[i].length == 2 
#  0 <= ai, bi < n 
#  ai != bi 
#  The given input represents a valid tree. 
#  
# 
#  Related Topics 树 深度优先搜索 图 动态规划 👍 393 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_dict = dict()
        for i in range(n):
            adj_dict[i] = []

        for x, y in edges:
            adj_dict[x].append(y)
            adj_dict[y].append(x)
        visited = [False] * n
        visited[0] = True
        d = [0] * n
        c = [1] * n

        def dfs(x: int):
            count = 1
            sub_dfs = 0
            if x not in adj_dict:
                d[x] = 0
                c[x] = 1
                return 0, 1
            for child in adj_dict[x]:
                if not visited[child]:
                    visited[child] = True
                    t1, t2 = dfs(child)
                    sub_dfs += t1
                    count += t2
            d[x] = sub_dfs + count - 1
            c[x] = count
            return sub_dfs + count - 1, count
        ans = [0] * n
        ans[0] = dfs(0)[0]
        visited = [False] * n
        visited[0] = True

        # change root
        def dfs2(root: int):
            for child in adj_dict[root]:
                if not visited[child]:
                    visited[child] = True
                    d_root, c_root = d[root], c[root]
                    d_child, c_child = d[child], c[child]
                    d[root] -= d[child] + c[child]
                    c[root] -= c[child]
                    d[child] += d[root] + c[root]
                    c[child] += c[root]
                    ans[child] = d[child]
                    dfs2(child)
                    # rollback
                    d[root], c[root] = d_root, c_root
                    d[child], c[child] = d_child, c_child
        dfs2(0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().sumOfDistancesInTree(n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
print(Solution().sumOfDistancesInTree(n=1, edges=[]))
print(Solution().sumOfDistancesInTree(n=2, edges=[[1, 0]]))
