# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find 
# all possible paths from node 0 to node n - 1 and return them in any order. 
# 
#  The graph is given as follows: graph[i] is a list of all nodes you can visit 
# from node i (i.e., there is a directed edge from node i to node graph[i][j]). 
# 
#  
#  Example 1: 
#  
#  
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
#  
# 
#  Example 2: 
#  
#  
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
#  
# 
#  
#  Constraints: 
# 
#  
#  n == graph.length 
#  2 <= n <= 15 
#  0 <= graph[i][j] < n 
#  graph[i][j] != i (i.e., there will be no self-loops). 
#  All the elements of graph[i] are unique. 
#  The input graph is guaranteed to be a DAG. 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 图 回溯 👍 394 👎 0
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        @cache
        def dfs(node: int) -> List[List[int]]:
            if node == graph.__len__() - 1:
                return [[node]]
            next_nodes = graph[node]
            ans = []
            for next_node in next_nodes:
                temp = [node]
                roads = dfs(next_node)
                for r in roads:
                    temp.extend(r)
                    ans.append(temp)
                    temp = [node]
            return ans

        return dfs(0)


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))
print(Solution().allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))
