import sys
from collections import deque
from functools import cache


def reverse(my_s: str, i: int) -> str:
    my_s = list(my_s)
    for idx in range(i + 1):
        my_s[idx] = str((int(my_s[idx]) + 1) % 2)
    return ''.join(my_s)


def c(ss: str) -> bool:
    return '1' not in ss or '0' not in ss


@cache
def to_target(target: str, s: str) -> int:
    s.rstrip(target)
    if s.__len__() == 0:
        return 0
    ans = 0
    count = s.count(target)
    for i in range(s.__len__()):
        ss = reverse(s, i)
        if ss.count(target) >= count:
            ans = min(ans, i + 1 + to_target(target, ss))
    return ans


class Solution:
    def minimumCost(self, s: str) -> int:
        if c(s):
            return 0
        n = s.__len__()
        pre_s = s[:n // 2]
        if n % 2 == 0:
            back_s = s[n // 2:]
        else:
            back_s = s[n // 2 + 1:][::-1]
        return min(to_target('0', pre_s) + to_target('0', back_s), to_target('1', pre_s) + to_target('1', back_s))


print(Solution().minimumCost('0011'))
print(Solution().minimumCost(s="010101"))
