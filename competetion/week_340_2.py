from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = nums.__len__()
        index_dict = dict()
        arr = [0] * n
        for idx, number in enumerate(nums):
            try:
                for i in index_dict[number]:
                    arr[i] += idx - i
                    arr[idx] += idx - i
                index_dict[number].append(idx)
            except KeyError:
                index_dict[number] = [idx]
        return arr


print(Solution().distance(nums=[1, 3, 1, 1, 2]))
print(Solution().distance(nums=[0, 5, 3]))
