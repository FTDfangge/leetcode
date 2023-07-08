from collections import defaultdict, deque
from typing import List


def findAllPaths(N, graph):
    # Initialize a dp array

    # Initialize it with 0
    dp = [[0 for _ in range(1 << N)] for _ in range(N)]

    # Initialize for the first vertex
    dp[0][1] = 1

    # Iterate over all the masks
    for i in range(2, (1 << N)):

        # If the first vertex is absent
        if ((i & (1 << 0)) == 0):
            continue

        # Only consider the full subsets
        if ((i & (1 << (N - 1))) and i != ((1 << N) - 1)):
            continue

        # Choose the end city
        for end in range(0, N):

            # If this city is not in the subset
            if (i & (1 << end) == 0):
                continue

                # Set without the end city
            prev = i - (1 << end)

            # Check for the adjacent cities

            for it in graph[end]:
                if ((i & (1 << it))):
                    dp[end][i] += dp[it][prev]

        # Print the answer
        return dp[N - 1][(1 << N) - 1]


def can_connect(n1: int, n2: int) -> bool:
    return n1 % n2 == 0 or n2 % n1 == 0


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = nums.__len__()
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if can_connect(nums[i], nums[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        return findAllPaths(n, graph)


print(Solution().specialPerm(nums=[2, 3, 6]))
# print(Solution().specialPerm(nums=[1, 4, 3]))
# print(Solution().specialPerm(
#     nums=[235745376, 19645448, 157163584, 471490752, 117872688, 589363440, 294681720, 147340860, 442022580, 73670430,
#           12278405, 110505645, 773539515, 257846505]))
