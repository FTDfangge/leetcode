# You are given an m x n matrix mat that has its rows sorted in non-decreasing 
# order and an integer k. 
# 
#  You are allowed to choose exactly one element from each row to form an array.
#  
# 
#  Return the kᵗʰ smallest array sum among all possible arrays. 
# 
#  
#  Example 1: 
# 
#  
# Input: mat = [[1,3,11],[2,4,6]], k = 5
# Output: 7
# Explanation: Choosing one element from each row, the first k smallest sum are:
# 
# [1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
#  
# 
#  Example 2: 
# 
#  
# Input: mat = [[1,3,11],[2,4,6]], k = 9
# Output: 17
#  
# 
#  Example 3: 
# 
#  
# Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
# Output: 9
# Explanation: Choosing one element from each row, the first k smallest sum are:
# 
# [1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th 
# sum is 9.  
#  
# 
#  
#  Constraints: 
# 
#  
#  m == mat.length 
#  n == mat.length[i] 
#  1 <= m, n <= 40 
#  1 <= mat[i][j] <= 5000 
#  1 <= k <= min(200, nᵐ) 
#  mat[i] is a non-decreasing array. 
#  
# 
#  Related Topics 数组 二分查找 矩阵 堆（优先队列） 👍 137 👎 0
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        h = []
        n = mat.__len__()
        count = 0
        for i in range(n):
            heapq.heappush(h, mat[i].pop(0))
        while count < k:
            count += 1

# leetcode submit region end(Prohibit modification and deletion)
