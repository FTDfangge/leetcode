from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, nums.__len__()):
            if nums[i] <= nums[i - 1]:
                ans += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        return ans


print(Solution().minOperations(nums=[1, 5, 2, 4, 1]))
