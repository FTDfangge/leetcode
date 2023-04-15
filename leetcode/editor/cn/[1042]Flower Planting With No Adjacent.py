# You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [
# xi, yi] describes a bidirectional path between garden xi to garden yi. In each 
# garden, you want to plant one of 4 types of flowers. 
# 
#  All gardens have at most 3 paths coming into or leaving it. 
# 
#  Your task is to choose a flower type for each garden such that, for any two 
# gardens connected by a path, they have different types of flowers. 
# 
#  Return any such a choice as an array answer, where answer[i] is the type of 
# flower planted in the (i+1)ᵗʰ garden. The flower types are denoted 1, 2, 3, or 4.
#  It is guaranteed an answer exists. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 3, paths = [[1,2],[2,3],[3,1]]
# Output: [1,2,3]
# Explanation:
# Gardens 1 and 2 have different types.
# Gardens 2 and 3 have different types.
# Gardens 3 and 1 have different types.
# Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2]
# , and [3,2,1].
#  
# 
#  Example 2: 
# 
#  
# Input: n = 4, paths = [[1,2],[3,4]]
# Output: [1,2,1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# Output: [1,2,3,4]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁴ 
#  0 <= paths.length <= 2 * 10⁴ 
#  paths[i].length == 2 
#  1 <= xi, yi <= n 
#  xi != yi 
#  Every garden has at most 3 paths coming into or leaving it. 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 图 👍 144 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        if not paths:
            return [(i % 4) + 1 for i in range(n)]

        colors = [0] * n
        adj_dict = dict()
        for x, y in paths:
            try:
                adj_dict[x - 1].append(y - 1)
            except KeyError:
                adj_dict[x - 1] = [y - 1]
            try:
                adj_dict[y - 1].append(x - 1)
            except KeyError:
                adj_dict[y - 1] = [x - 1]

        def dfs(current: int):
            flowers = [1, 2, 3, 4]
            next_garden = []
            try:
                for neighbor in adj_dict[current]:
                    if colors[neighbor]:
                        try:
                            flowers.remove(colors[neighbor])
                        except ValueError:
                            pass
                    else:
                        next_garden.append(neighbor)
            except KeyError:
                pass
            if not flowers:
                return False
            if not next_garden:
                colors[current] = flowers[0]
                return True
            for f in flowers:
                colors[current] = f
                for n in next_garden:
                    if not dfs(n):
                        break
                else:
                    return True
            return False

        for i in range(n):
            dfs(i)
        return colors


# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().gardenNoAdj(n=3, paths=[[1, 2], [2, 3], [3, 1]]))
# print(Solution().gardenNoAdj(n=4, paths=[[1, 2], [3, 4]]))
# print(Solution().gardenNoAdj(n=4, paths=[[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]))
print(Solution().gardenNoAdj(5, [[4, 1], [4, 2], [4, 3], [2, 5], [1, 2], [1, 5]]))
