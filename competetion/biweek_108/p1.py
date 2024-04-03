from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        def check(start, end):
            pre_diff = -1
            for ii in range(start, end):
                if nums[ii + 1] - nums[ii] != -pre_diff:
                    return False
                else:
                    pre_diff = -pre_diff
            return True

        ans = -1
        n = nums.__len__()
        for i in range(n):
            for j in range(i + 1, n):
                if check(i, j):
                    ans = max(ans, j - i + 1)
        return ans


print(Solution().alternatingSubarray(nums=[2, 3, 4, 3, 4]))
print(Solution().alternatingSubarray(nums=[4, 5, 6]))
print(Solution().alternatingSubarray([31, 32, 31, 32, 33]))
