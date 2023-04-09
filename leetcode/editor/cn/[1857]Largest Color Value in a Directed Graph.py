# There is a directed graph of n colored nodes and m edges. The nodes are 
# numbered from 0 to n - 1. 
# 
#  You are given a string colors where colors[i] is a lowercase English letter 
# representing the color of the iᵗʰ node in this graph (0-indexed). You are also 
# given a 2D array edges where edges[j] = [aj, bj] indicates that there is a 
# directed edge from node aj to node bj. 
# 
#  A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk 
# such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The 
# color value of the path is the number of nodes that are colored the most 
# frequently occurring color along that path. 
# 
#  Return the largest color value of any valid path in the given graph, or -1 
# if the graph contains a cycle. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (
# red in the above image).
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: colors = "a", edges = [[0,0]]
# Output: -1
# Explanation: There is a cycle from 0 to 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == colors.length 
#  m == edges.length 
#  1 <= n <= 10⁵ 
#  0 <= m <= 10⁵ 
#  colors consists of lowercase English letters. 
#  0 <= aj, bj < n 
#  
# 
#  Related Topics 图 拓扑排序 记忆化搜索 哈希表 动态规划 计数 👍 39 👎 0
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj_dict = dict()
        no_pre = [i for i in range(colors.__len__())]
        for x, y in edges:
            try:
                no_pre.remove(y)
            except ValueError:
                pass
            try:
                adj_dict[x].append(y)
            except KeyError:
                adj_dict[x] = [y]

        paths = []
        if not no_pre:
            return -1

        @cache
        def dfs(root: int, path: tuple):
            neighbors = []
            try:
                neighbors = adj_dict[root]
            except KeyError:
                paths.append(tuple(list(path) + [root]))
                return
            for n in neighbors:
                if n in path:
                    return -1
                dfs(n, tuple(list(path) + [root]))

        for i in no_pre:
            if dfs(i, ()) == -1:
                return -1
        max_color_value = 0
        for p in paths:
            temp_dict = dict()
            for node in p:
                try:
                    temp_dict[colors[node]] += 1
                except KeyError:
                    temp_dict[colors[node]] = 1
            color_vars = list(temp_dict.values())
            color_vars.sort(reverse=True)
            max_color_value = max(max_color_value, color_vars[0])
        return max_color_value


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().largestPathValue(colors="abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]]))
print(Solution().largestPathValue(colors="a", edges=[[0, 0]]))
