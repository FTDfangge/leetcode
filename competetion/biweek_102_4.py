import heapq
import sys
from collections import deque
from typing import List


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj_dict = dict()
        for i in range(n):
            self.adj_dict[i] = []
        for x, y, cost in edges:
            self.adj_dict[x].append((y, cost))

    def addEdge(self, edge: List[int]) -> None:
        self.adj_dict[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        def dijkstra(src):
            distance = [sys.maxsize] * self.n
            distance[src] = 0
            spt_set = [False] * self.n
            q = [(0, src)]
            while q:
                current_dis, current = heapq.heappop(q)
                spt_set[current] = True
                for next_node, next_dis in self.adj_dict[current]:
                    if not spt_set[next_node] and distance[next_node] > current_dis + next_dis:
                        distance[next_node] = current_dis + next_dis
                        heapq.heappush(q, (distance[next_node], next_node))
            return distance
        ans = dijkstra(node1)[node2]
        return ans if ans != sys.maxsize else -1
