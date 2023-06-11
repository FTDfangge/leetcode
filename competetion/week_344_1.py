from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        front = []
        s = set()
        for i in nums:
            s.add(i)
            front.append(s.__len__())
        total = s.__len__()
        back = []
        s = set()
        for i in nums[::-1]:
            s.add(i)
            back.append(s.__len__())
        back = back[::-1]
        diff = []
        for i in range(front.__len__() - 1):
            diff.append(front[i] - back[i + 1])
        diff.append(front[-1])
        return diff


print(Solution().distinctDifferenceArray([1, 2, 3, 4, 5]))
print(Solution().distinctDifferenceArray([3, 2, 3, 4, 2]))
