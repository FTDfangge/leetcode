from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            t = list(map(int, list(str(i))))
            t = int('1' * t.__len__()) * max(t)
            s += t
        return s


print(Solution().sumOfEncryptedInt([1, 2, 3]))
print(Solution().sumOfEncryptedInt([10, 21, 31]))
