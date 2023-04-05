# Given an n x n binary matrix grid, return the length of the shortest clear 
# path in the matrix. If there is no clear path, return -1. 
# 
#  A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0
# )) to the bottom-right cell (i.e., (n - 1, n - 1)) such that: 
# 
#  
#  All the visited cells of the path are 0. 
#  All the adjacent cells of the path are 8-directionally connected (i.e., they 
# are different and they share an edge or a corner). 
#  
# 
#  The length of a clear path is the number of visited cells of this path. 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[0,1],[1,0]]
# Output: 2
#  
# 
#  Example 2: 
#  
#  
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
#  
# 
#  
#  Constraints: 
# 
#  
#  n == grid.length 
#  n == grid[i].length 
#  1 <= n <= 100 
#  grid[i][j] is 0 or 1 
#  
# 
#  Related Topics 广度优先搜索 数组 矩阵 👍 259 👎 0
import sys
from collections import deque
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[-1][-1] != 0 or grid[0][0] != 0:
            return -1

        n = grid.__len__()
        distance = [[sys.maxsize] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        distance[-1][-1] = 1
        visited[-1][-1] = True
        q = deque([[n - 1, n - 1, 1]])
        while q:
            x, y, dis = q.popleft()
            # top left
            if x >= 1 and y >= 1 and grid[x - 1][y - 1] == 0 and not visited[x - 1][y - 1]:
                distance[x - 1][y - 1] = dis + 1
                q.append([x - 1, y - 1, dis + 1])
                visited[x - 1][y - 1] = True
            # top
            if x >= 1 and grid[x - 1][y] == 0 and not visited[x - 1][y]:
                distance[x - 1][y] = dis + 1
                q.append([x - 1, y, dis + 1])
                visited[x - 1][y] = True
            # top right
            if x >= 1 and y < n - 1 and grid[x - 1][y + 1] == 0 and not visited[x - 1][y + 1]:
                distance[x - 1][y + 1] = dis + 1
                q.append([x - 1, y + 1, dis + 1])
                visited[x - 1][y + 1] = True
            # left
            if y >= 1 and grid[x][y - 1] == 0 and not visited[x][y - 1]:
                distance[x][y - 1] = dis + 1
                q.append([x, y - 1, dis + 1])
                visited[x][y - 1] = True
            # right
            if y < n - 1 and grid[x][y + 1] == 0 and not visited[x][y + 1]:
                distance[x][y + 1] = dis + 1
                q.append([x, y + 1, dis + 1])
                visited[x][y + 1] = True
            # bottom left
            if x < n - 1 and y >= 1 and grid[x + 1][y - 1] == 0 and not visited[x + 1][y - 1]:
                distance[x + 1][y - 1] = dis + 1
                q.append([x + 1, y - 1, dis + 1])
                visited[x + 1][y - 1] = True
            # bottom
            if x < n - 1 and grid[x + 1][y] == 0 and not visited[x + 1][y]:
                distance[x + 1][y] = dis + 1
                q.append([x + 1, y, dis + 1])
                visited[x + 1][y] = True
            # bottom right
            if x < n - 1 and y < n - 1 and grid[x + 1][y + 1] == 0 and not visited[x + 1][y + 1]:
                distance[x + 1][y + 1] = dis + 1
                q.append([x + 1, y + 1, dis + 1])
                visited[x + 1][y + 1] = True
        return distance[0][0] if distance[0][0] != sys.maxsize else -1


# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().shortestPathBinaryMatrix(grid=[[0, 1], [1, 0]]))
# print(Solution().shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(Solution().shortestPathBinaryMatrix([[0, 1, 1, 0, 0, 0],
                                           [0, 1, 0, 1, 1, 0],
                                           [0, 1, 1, 0, 1, 0],
                                           [0, 0, 0, 1, 1, 0],
                                           [1, 1, 1, 1, 1, 0],
                                           [1, 1, 1, 1, 1, 0]]))
