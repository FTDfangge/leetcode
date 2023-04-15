import sys
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_dict = dict()
        for f in flights:
            if f[0] in flight_dict:
                flight_dict[f[0]].append([f[1], f[2]])
            else:
                flight_dict[f[0]] = [[f[1], f[2]]]

        min_price = sys.maxsize
        q = [[src, -1, 0, [src]]]  # first is current node, second is stops, third is price, forth is path
        while q:
            current, stops, price, path = q.pop(0)
            if current in flight_dict:
                for i in flight_dict[current]:
                    if i[0] not in path:
                        if price + i[1] >= min_price:
                            continue
                        elif stops + 1 > k:
                            continue
                        elif i[0] == dst:
                            min_price = min(min_price, price + i[1])
                        else:
                            q.append([i[0], stops + 1, price + i[1], path + [i[0]]])
        return min_price if min_price != sys.maxsize else -1


print(
    Solution().findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1) == 700)
print(Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                                   src=0, dst=2, k=1) == 200)
print(Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                                   src=0, dst=2, k=0) == 500)
print(Solution().findCheapestPrice(15,
                                   [[10, 14, 43], [1, 12, 62], [4, 2, 62], [14, 10, 49], [9, 5, 29], [13, 7, 53],
                                    [4, 12, 90], [14, 9, 38], [11, 2, 64], [2, 13, 92], [11, 5, 42], [10, 1, 89],
                                    [14, 0, 32], [9, 4, 81], [3, 6, 97], [7, 13, 35], [11, 9, 63], [5, 7, 82],
                                    [13, 6, 57], [4, 5, 100], [2, 9, 34], [11, 13, 1], [14, 8, 1], [12, 10, 42],
                                    [2, 4, 41], [0, 6, 55], [5, 12, 1], [13, 3, 67], [3, 13, 36], [3, 12, 73],
                                    [7, 5, 72], [5, 6, 100], [7, 6, 52], [4, 7, 43], [6, 3, 67], [3, 1, 66],
                                    [8, 12, 30], [8, 3, 42], [9, 3, 57], [12, 6, 31], [2, 7, 10], [14, 4, 91],
                                    [2, 3, 29], [8, 9, 29], [2, 11, 65], [3, 8, 49], [6, 14, 22], [4, 6, 38],
                                    [13, 0, 78], [1, 10, 97], [8, 14, 40], [7, 9, 3], [14, 6, 4], [4, 8, 75],
                                    [1, 6, 56]],
                                   1,
                                   4,
                                   10) == 169)

