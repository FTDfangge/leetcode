from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        banned = []
        for idx, val in enumerate(nums):
            if val < minK or val > maxK:
                banned.append(idx)
        banned.append(nums.__len__())
        pre_banned = -1
        ans = 0
        for ban in banned:
            min_pos = []
            max_pos = []
            for i in range(pre_banned + 1, ban):
                if nums[i] == minK:
                    min_pos.append(i)
                if nums[i] == maxK:
                    max_pos.append(i)
            ptr_min = 0
            ptr_max = 0
            for i in range(pre_banned + 1, ban):
                if ptr_min not in range(min_pos.__len__()):
                    break
                if ptr_max not in range(max_pos.__len__()):
                    break
                min_end = max(min_pos[ptr_min], max_pos[ptr_max])
                ans += ban - min_end
                # print('start: ', i, ' count is ', ban - min_end)
                if min_pos[ptr_min] == i:
                    ptr_min += 1
                if max_pos[ptr_max] == i:
                    ptr_max += 1
            pre_banned = ban
        return ans


print(Solution().countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5))
print(Solution().countSubarrays(nums=[1, 1, 1, 1], minK=1, maxK=1))
