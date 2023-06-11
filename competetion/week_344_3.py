import bisect
from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        nums = [0] * n
        color_range = dict()

        def add_color(c: int, index: int):
            if c not in color_range:
                color_range[c] = [[index, index]]
            else:
                starts = [i[0] for i in color_range[c]]
                ends = [i[1] for i in color_range[c]]
                target = bisect.bisect_left(starts, index) - 1
                if target == -1:
                    color_range[c] = [[index, index]] + color_range[c]
                if ends[target] >= index:
                    return
                elif ends[target] + 1 == index:
                    if target + 1 < starts.__len__() and index + 1 == starts[target + 1]:
                        color_range[c][target:target + 2] = [[starts[target], ends[target + 1]]]
                    else:
                        color_range[c][target][1] += 1
                else:
                    if target + 1 < starts.__len__() and index + 1 == starts[target + 1]:
                        color_range[c][target + 1][0] -= 1
                    else:
                        color_range[c][target:target + 1] = [color_range[c][target], [index, index]]

        def remove_color(c: int, index: int):
            starts = [i[0] for i in color_range[c]]
            ends = [i[1] for i in color_range[c]]
            target = bisect.bisect_left(starts, index) - 1
            if starts[target] == ends[target]:
                color_range[c].pop(target)
            else:
                if starts[target] == index:
                    color_range[c][target][0] += 1
                elif ends[target] == index:
                    color_range[c][target][1] -= 1
                else:
                    color_range[c][target:target + 1] = [[starts[target], index - 1], [index + 1, ends[target]]]
            if not color_range[c]:
                color_range.pop(c)

        def get_ans() -> int:
            res = 0
            for i in color_range.items():
                for s, e in i[1]:
                    res += e - s
            return res

        ans = []
        for idx, color in queries:
            if not nums[idx] == 0:
                remove_color(nums[idx], idx)
            nums[idx] = color
            # print('test', nums)
            add_color(color, idx)
            ans.append(get_ans())
        return ans


# print(Solution().colorTheArray(n=4, queries=[[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]]))
# print(Solution().colorTheArray(n=1, queries=[[0, 100000]]))
print(Solution().colorTheArray(8,
                               [[6, 2], [2, 1], [0, 6], [0, 1], [0, 4], [0, 1], [5, 7], [5, 3], [7, 6], [6, 7], [0, 4],
                                [4, 6], [4, 2], [3, 7], [4, 4], [5, 1]]))
