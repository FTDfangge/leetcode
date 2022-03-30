# -*- coding: utf-8 -*-
# @Time    : 2022-03-30 10:51 a.m.
# @Author  : qkzhong
# @FileName: 1606_busiest_servers.py
# @Software: PyCharm
import heapq

from sortedcontainers import SortedList
from typing import List


class Solution:

    # O(n*k) takes too long
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # construct server matrix, which stores the server's latest available time
        servers = [0 for i in range(k)]
        server_missions = [0 for i in range(k)]

        # allocate each mission to every server
        for i in range(arrival.__len__()):
            for server_number in list(range(i % k, k)) + list(range(i % k)):
                if arrival[i] >= servers[server_number]:  # free server
                    # allocate this mission to this server
                    servers[server_number] = arrival[i] + load[i]
                    server_missions[server_number] += 1
                    break

        # find the busiestServer
        m = max(server_missions)
        res = []
        for i in range(server_missions.__len__()):
            if server_missions[i] == m:
                res.append(i)

        return res

    def busiestServers2(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k))
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                available.add(busy[0][1])
                heapq.heappop(busy)
            if len(available) == 0:
                continue
            j = available.bisect_left(i % k)
            if j == len(available):
                j = 0
            id = available[j]
            requests[id] += 1
            heapq.heappush(busy, (start + t, id))
            available.remove(id)
        maxRequest = max(requests)
        return [i for i, req in enumerate(requests) if req == maxRequest]


print(Solution().busiestServers2(3,
[1,2,3,4,5],
[5,2,3,3,3]))
