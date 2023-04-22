from typing import List


class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        def merge():
            sum_list = []
            for i in range(1, supplies.__len__()):
                sum_list.append(supplies[i - 1] + supplies[i])
            min_idx = 0
            min_val = sum_list[0]
            idx = 0
            while idx < sum_list.__len__():
                if sum_list[idx] < min_val:
                    min_val = sum_list[idx]
                    min_idx = idx
                idx += 1
            supplies[min_idx:min_idx + 2] = [min_val]

        length = supplies.__len__()
        target = length // 2
        while length > target:
            merge()
            length = supplies.__len__()
        return supplies


print(Solution().supplyWagon(supplies=[7, 3, 6, 1, 8]))
print(Solution().supplyWagon(supplies=[1, 3, 1, 5]))
