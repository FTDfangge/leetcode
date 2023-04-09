import sys
from typing import List


class Solution:  # 65 / 1582
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()

        def dfs(remain_nums: List[int], remain_pairs: int) -> List[List[int]]:
            if remain_pairs:
                n = remain_nums.__len__()
                diffs = []
                for i in range(1, n):
                    for j in range(i):
                        diff = -remain_nums[j] + remain_nums[i]
                        remain = dfs(remain_nums[:j] + remain_nums[j + 1: i] + remain_nums[i + 1:], remain_pairs - 1)
                        if remain:
                            for r in remain:
                                diffs.append([diff] + r)
                        else:
                            diffs.append([diff])
                return diffs
            else:
                return []

        possible_diffs = dfs(nums, p)
        for poss in possible_diffs:
            poss.sort()
        ans = sys.maxsize
        for i in range(possible_diffs.__len__()):
            ans = min(ans, possible_diffs[i][p - 1])
        return ans


class Solution2:  # 1095 / 1582
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        possible_diffs = []
        appeared = dict()
        n = nums.__len__()
        for i in range(1, n):
            for j in range(i):
                possible_diffs.append(abs(nums[j] - nums[i]))
        possible_diffs.sort()
        return possible_diffs[p - 1]


# print(Solution().minimizeMax(nums=[10, 1, 2, 7, 1, 3], p=2))
# print(Solution().minimizeMax(nums=[4, 2, 1, 2], p=1))
# print(Solution().minimizeMax(nums=[0, 5, 3, 4], p=0))
# print(Solution().minimizeMax([3, 4, 2, 3, 2, 1, 2], 3))
print(Solution().minimizeMax([1, 1, 0, 3], 2))
