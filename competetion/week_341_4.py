import copy
import sys
from collections import deque
from typing import List


def add_to_dict(k, v, dic):
    try:
        dic[k].append(v)
    except KeyError:
        dic[k] = [v]


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        adj_dict = dict()
        for x, y in edges:
            add_to_dict(x, y, adj_dict)
            add_to_dict(y, x, adj_dict)

        all_node = [i for i in range(n)]
        discount = set()

        def get_dis(start: int, nodes: List[int]) -> List[List[int]]:
            if nodes.__len__() == 1:
                return [nodes]

            # discount node i
            ans = []
            other = copy.deepcopy(nodes)
            other.remove(start)
            for adj in adj_dict[start]:
                try:
                    other.remove(adj)
                except ValueError:
                    pass
            for o in other:
                temp = get_dis(o, other)
                for t in temp:
                    ans.append([start] + t)
            if not ans:
                return [[start]]
            return ans

        for i in range(n):
            temp = get_dis(i, all_node)
            for t in temp:
                t.sort()
                discount.add(tuple(t))
        discount = list(discount)
        ans = sys.maxsize

        def get_routine(start: int, end: int):
            if start == end:
                return [start]
            visited = [False] * n
            q = deque([[start, [start]]])
            visited[start] = True
            while q:
                current, routine = q.popleft()
                for adj in adj_dict[current]:
                    if adj == end:
                        return routine + [adj]
                    if not visited[adj]:
                        visited[adj] = True
                        q.append([adj, routine + [adj]])
            return -1

        def get_trip_routine(t: List[List[int]]):
            total = []
            for start, end in t:
                total.extend(get_routine(start, end))
            return total

        routine = get_trip_routine(trips)
        
        return ans


print(Solution().minimumTotalPrice(n=4, edges=[[0, 1], [1, 2], [1, 3]], price=[2, 2, 10, 6],
                                   trips=[[0, 3], [2, 1], [2, 3]]))
print(Solution().minimumTotalPrice(n=2, edges=[[0, 1]], price=[2, 2], trips=[[0, 0]]))
