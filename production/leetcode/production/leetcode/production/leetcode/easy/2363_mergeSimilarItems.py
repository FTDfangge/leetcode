from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        item_dict = dict()
        for val, weight in items1 + items2:
            try:
                item_dict[val] += weight
            except KeyError:
                item_dict[val] = weight
        ans = sorted(item_dict.items(), key=lambda x: x[0])
        return list(map(list, ans))


print(Solution().mergeSimilarItems(items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]]))
