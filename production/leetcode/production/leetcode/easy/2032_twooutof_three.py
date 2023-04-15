from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = set()
        for i in nums1:
            if i in nums2 or i in nums3:
                res.add(i)
        for i in nums2:
            if i in nums3:
                res.add(i)

        return list(res)


print(Solution().twoOutOfThree(nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]))
