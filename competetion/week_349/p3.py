import sys
from typing import List


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        def shift():
            nonlocal nums
            nums = nums[1:] + [nums[0]]

        def undo_shift():
            nonlocal nums
            nums = [nums[-1]] + nums[:-1]

        n = nums.__len__()

        def find_min():
            mi = sys.maxsize
            min_idx = -1
            for idx, i in enumerate(nums):
                if not bought[idx] and i < mi:
                    mi = i
                    min_idx = idx
            return min_idx

        def get_min_cost(have: List[int]) -> int:
            if False not in have:
                return 0
            # not shift and buy
            m_idx_1 = find_min()
            have[m_idx_1] = True
            cost_1 = nums[m_idx_1] + get_min_cost(have)
            have[m_idx_1] = False

            # shift and buy
            shift()
            m_idx_2 = find_min()
            have[m_idx_2] = True
            cost_2 = x + nums[m_idx_2] + get_min_cost(have)
            have[m_idx_2] = False
            undo_shift()
            return min(cost_1, cost_2)

        bought = [False] * n
        return get_min_cost(bought)


print(Solution().minCost(nums=[20, 1, 15], x=5))
# print(Solution().minCost(nums=[1, 2, 3], x=4))
# print(Solution().minCost([31, 25, 18, 59], 27))
print(Solution().minCost([271, 902, 792, 501, 184, 559, 140, 506, 94, 161],
                         167))
