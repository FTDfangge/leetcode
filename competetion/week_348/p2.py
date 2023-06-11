from bisect import bisect_left
from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = nums.__len__()
        for i in range(n):
            if nums[i] == 1:
                idx_1 = i
            if nums[i] == n:
                idx_n = i
        s = idx_1 - 0 + n - 1 - idx_n
        if idx_1 > idx_n:
            s -= 1
        return s


print(Solution().semiOrderedPermutation(nums=[2, 1, 4, 3]))
