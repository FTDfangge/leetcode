from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = s.__len__()
        final_shift = 0
        for i in shift:
            if i[0] == 0:
                final_shift += i[1]
            else:
                final_shift -= i[1]
        s = s[final_shift % n:] + s[:final_shift % n]
        return s


print(Solution().stringShift(s="abc", shift=[[0, 1], [1, 2]]) == 'cab')
print(Solution().stringShift(s="abc", shift=[[0, 1]]) == 'bca')
print(Solution().stringShift("xqgwkiqpif",
                             [[1, 4], [0, 7], [0, 8], [0, 7], [0, 6], [1, 3], [0, 1], [1, 7], [0, 5],
                              [0, 6]]) == 'qpifxqgwki')
