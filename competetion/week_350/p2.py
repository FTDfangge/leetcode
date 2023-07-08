import sys
from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        diff = sys.maxsize
        for i in range(nums.__len__() - 1):
            diff = min(diff, abs(nums[i + 1] - nums[i]))
        return diff


print(Solution().findValueOfPartition(nums=[1, 3, 2, 4]))
print(Solution().findValueOfPartition(nums=[100, 1, 10]))
