# 力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。它们之间以 服务器到服务器 的形式相互连接组成了一个内部集群，连接是无向的。用 
# connections 表示集群网络，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。任何服务器都可以直接或者间接地通过网络
# 到达任何其他服务器。 
# 
#  关键连接 是在该集群中的重要连接，假如我们将它移除，便会导致某些服务器无法访问其他服务器。 
# 
#  请你以任意顺序返回该集群内的所有 关键连接 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# 输出：[[1,3]]
# 解释：[[3,1]] 也是正确的。 
# 
#  示例 2: 
# 
#  
# 输入：n = 2, connections = [[0,1]]
# 输出：[[0,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 10⁵ 
#  n - 1 <= connections.length <= 10⁵ 
#  0 <= ai, bi <= n - 1 
#  ai != bi 
#  不存在重复的连接 
#  
# 
#  Related Topics 深度优先搜索 图 双连通分量 👍 228 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        id_list = [-1] * n
        id_list[0] = 0
        g = [[] for _ in range(n)]
        res = []
        for i, j in connections:
            g[i].append(j)
            g[j].append(i)

        def dfs(cur, node_id, pre):
            id_list[cur] = node_id
            for ne in g[cur]:
                if ne == pre:
                    continue
                if id_list[ne] == -1:
                    dfs(ne, node_id + 1, cur)
                if id_list[ne] < id_list[cur]:
                    id_list[cur] = id_list[ne]
            if node_id == id_list[cur] and pre is not None:
                res.append([pre, cur])

        dfs(0, 0, None)
        return res


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]))
