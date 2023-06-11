from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        s = 0
        r_val = dict()
        c_val = dict()
        sum_row = dict()
        sum_col = dict()
        intersections = dict()
        for t, i, v in queries:
            s += n * v
            if t == 0:
                # row
                if i not in r_val:
                    sum_row[i] = n * v
                    r_val[i] = v
                    for key, val in c_val.items():
                        sum_col[key] = sum_col[key] - val + v
                        intersections[(i, key)] = v
                        s -= val
            else:
                # col
                if i not in c_val:
                    sum_col[i] = n * v
                    c_val[i] = v
                    for key, val in r_val.items():
                        sum_row[key] = sum_row[key] - val + v
                        intersections[(key, i)] = v
                        s -= val


print(Solution().matrixSumQueries(n=3, queries=[[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4], [0, 0, 1]]))
