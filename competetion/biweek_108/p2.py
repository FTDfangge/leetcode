from typing import List


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        pos_dict = dict()
        for i in nums:
            try:
                pos_dict[i] += 1
            except KeyError:
                pos_dict[i] = 1
        n = moveFrom.__len__()
        for op in range(n):
            number_of_marbles = pos_dict.pop(moveFrom[op])
            try:
                pos_dict[moveTo[op]] += number_of_marbles
            except KeyError:
                pos_dict[moveTo[op]] = number_of_marbles
        return sorted(pos_dict.keys())


print(Solution().relocateMarbles(nums=[1, 6, 7, 8], moveFrom=[1, 7, 2], moveTo=[2, 9, 5]))
