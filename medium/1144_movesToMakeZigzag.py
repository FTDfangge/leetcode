from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if nums.__len__() <= 1:
            return 0
        n = nums.__len__()
        even_ops = 0
        for i in range(1, n, 2):
            should_change = 0
            if i + 1 < n:
                should_change = nums[i] - min(nums[i - 1], nums[i + 1])
            else:
                should_change = nums[i] - nums[i - 1]
            if should_change >= 0:
                even_ops += should_change + 1

        odd_ops = 0
        odd_ops += nums[0] - nums[1] + 1 if nums[0] - nums[1] >= 0 else 0
        for i in range(2, n, 2):
            should_change = 0
            if i + 1 < n:
                should_change = nums[i] - min(nums[i - 1], nums[i + 1])
            else:
                should_change = nums[i] - nums[i - 1]
            if should_change >= 0:
                odd_ops += should_change + 1
        return min(even_ops, odd_ops)


print(Solution().movesToMakeZigzag(nums=[1, 2, 3]))
print(Solution().movesToMakeZigzag(nums=[9, 6, 1, 6, 2]))
print(Solution().movesToMakeZigzag(nums=[1]))
