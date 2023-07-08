import bisect
from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        servers = dict()
        logs.sort(key=lambda x: x[1])
        for i in range(n):
            servers[i + 1] = []
        for server_id, time in logs:
            servers[server_id].append(time)
        ans = []
        for q in queries:
            count = 0
            for s in servers.keys():
                if servers[s]:
                    bi = bisect.bisect_left(servers[s], q - x)
                    if bi < servers[s].__len__() and servers[s][bi] <= q:
                        continue
                    else:
                        count += 1
                else:
                    count += 1
            ans.append(count)
        return ans


print(Solution().countServers(n=3, logs=[[1, 3], [2, 6], [1, 5]], x=5, queries=[10, 11]))
print(Solution().countServers(n=3, logs=[[2, 4], [2, 1], [1, 2], [3, 1]], x=2, queries=[3, 4]))
