import heapq
from typing import List


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        q = []
        for idx, i in enumerate(nums):
            heapq.heappush(q, (i, idx))
        n = nums.__len__()
        marked = [False] * n
        remain = sum(nums)
        ans = []
        for index, k in queries:
            if not marked[index]:
                marked[index] = True
                remain = remain - nums[index]
            for _ in range(k):
                try:
                    number, i = heapq.heappop(q)
                    while marked[i]:
                        number, i = heapq.heappop(q)
                    marked[i] = True
                    remain -= number
                except IndexError:
                    break
            ans.append(remain)
        return ans


print(Solution().unmarkedSumArray(nums=[1, 2, 2, 1, 2, 3, 1], queries=[[1, 2], [3, 3], [4, 2]]))
print(Solution().unmarkedSumArray(nums=[1, 4, 2, 3], queries=[[0, 1]]))
