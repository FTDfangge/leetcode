from collections import deque
from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        total = sum(nums)
        if total % k != 0:
            return False
        for i in range(1, nums.__len__() - 1):
            if min(abs(nums[i] - nums[i - 1]), abs(nums[i + 1] - nums[i])) >= 2:
                return False

        return True


print(Solution().checkArray(nums=[2, 2, 3, 1, 1, 0], k=3))
