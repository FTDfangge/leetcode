from typing import List


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = nums1.__len__()
        ans = 1
        # new nums1 and nums2
        for ii in range(n):
            mi = min(nums1[ii], nums2[ii])
            ma = max(nums1[ii], nums2[ii])
            nums1[ii], nums2[ii] = mi, ma
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, n):
            # dp[i][0]
            temp = 1
            if nums1[i] >= nums1[i - 1]:
                temp = max(temp, dp[i - 1][0] + 1)
            if nums1[i] >= nums2[i - 1]:
                temp = max(temp, dp[i - 1][1] + 1)
            dp[i][0] = temp
            # dp[i][1]
            temp = 1
            if nums2[i] >= nums1[i - 1]:
                temp = max(temp, dp[i - 1][0] + 1)
            if nums2[i] >= nums2[i - 1]:
                temp = max(temp, dp[i - 1][1] + 1)
            dp[i][1] = temp
            # refresh ans
            ans = max(ans, *dp[i])

        return ans


print(Solution().maxNonDecreasingLength(nums1=[2, 3, 1], nums2=[1, 2, 1]))
