from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        max_arr = []
        temp_max = 0
        conver = []
        ans = [0]
        for i in nums:
            temp_max = max(temp_max, i)
            max_arr.append(temp_max)
            conver.append(i + max_arr[-1])
            ans.append(ans[-1] + conver[-1])
        return ans[1:]


print(Solution().findPrefixScore([2, 3, 7, 5, 10]))
print(Solution().findPrefixScore(nums=[1, 1, 2, 4, 8, 16]))
