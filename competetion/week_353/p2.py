from functools import cache
from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        next_dict = dict()
        n = nums.__len__()
        for ii in range(n):
            for jj in range(ii + 1, n):
                if abs(nums[jj] - nums[ii]) <= target:
                    try:
                        next_dict[ii].append(jj)
                    except KeyError:
                        next_dict[ii] = [jj]

        @cache
        def dp(i: int) -> int:
            if i == n - 1:
                return 0
            max_jumps = -1
            if i not in next_dict:
                return -1
            for nn in next_dict[i]:
                next_jumps = dp(nn)
                if next_jumps != -1:
                    max_jumps = max(max_jumps, 1 + dp(nn))
            return max_jumps

        return dp(0)


print(Solution().maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=2))
print(Solution().maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=3))
print(Solution().maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=0))
print(Solution().maximumJumps([1, 0, 2], 1))
