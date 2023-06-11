from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        positive = list(filter(lambda x: x > 0, nums))
        ans = 1
        for i in positive:
            ans *= i
        negative = list(filter(lambda x: x < 0, nums))
        negative.sort()
        if negative.__len__() % 2 == 0:
            pass
        else:
            negative.pop()
        if not negative and not positive:
            return max(nums)
        for j in negative:
            ans *= j
        return ans


print(Solution().maxStrength(nums=[3, -1, -5, 2, 5, -9]))
print(Solution().maxStrength(nums=[0, -1]))
print(Solution().maxStrength(nums=[-9]))
print(Solution().maxStrength(nums=[0]))
