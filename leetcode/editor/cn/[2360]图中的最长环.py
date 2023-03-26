# 给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，其中每个节点 至多 有一条出边。 
# 
#  图用一个大小为 n 下标从 0 开始的数组 edges 表示，节点 i 到节点 edges[i] 之间有一条有向边。如果节点 i 没有出边，那么 
# edges[i] == -1 。 
# 
#  请你返回图中的 最长 环，如果没有任何环，请返回 -1 。 
# 
#  一个环指的是起点和终点是 同一个 节点的路径。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：edges = [3,3,4,2,3]
# 输出去：3
# 解释：图中的最长环是：2 -> 4 -> 3 -> 2 。
# 这个环的长度为 3 ，所以返回 3 。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：edges = [2,-1,3,1]
# 输出：-1
# 解释：图中没有任何环。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == edges.length 
#  2 <= n <= 10⁵ 
#  -1 <= edges[i] < n 
#  edges[i] != i 
#  
# 
#  Related Topics 深度优先搜索 图 拓扑排序 👍 27 👎 0
import sys
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = edges.__len__()
        visit_time = [0] * n
        clock = 1
        longest_cycle = -1
        for node in range(n):
            if visit_time[node] > 0:
                continue
            # this node is not visited yet
            ptr = edges[node]
            start = clock
            while ptr >= 0:

                if visit_time[ptr] > 0:
                    if visit_time[ptr] >= start:  # cycle found
                        longest_cycle = max(longest_cycle, clock - visit_time[ptr])
                    break
                visit_time[ptr] = clock
                clock += 1
                ptr = edges[ptr]
        return longest_cycle


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().longestCycle(edges=[3, 3, 4, 2, 3]))
print(Solution().longestCycle(edges=[2, -1, 3, 1]))
print(Solution().longestCycle([1, 2, 0, 4, 5, 6, 3, 8, 9, 7]))
print(Solution().longestCycle([-1, 4, -1, 2, 0, 4]))
