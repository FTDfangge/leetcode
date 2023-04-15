from typing import List


def add_to_sorted_list(l: List[int], target) -> List[int]:
    if not l:
        return [target]
    mid = l.__len__() // 2
    if l[mid] == target:
        return l
    elif mid + 1 < l.__len__() and l[mid + 1] == target:
        return l
    elif mid + 1 < l.__len__() and l[mid] < target < l[mid + 1]:
        l[mid + 1:mid + 1] = [target]
        return l
    elif l[mid] > target:
        return add_to_sorted_list(l[:mid], target) + l[mid:]
    elif mid + 1 < l.__len__() and l[mid + 1] < target:
        return l[:mid + 1] + add_to_sorted_list(l[mid + 1:], target)
    elif mid + 1 == l.__len__():
        return l + [target]


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        sorted_list = [1]
        count = 0
        ans = 0
        while count < n:
            ans = sorted_list.pop(0)
            count += 1
            sorted_list = add_to_sorted_list(sorted_list, ans * 2)
            sorted_list = add_to_sorted_list(sorted_list, ans * 3)
            sorted_list = add_to_sorted_list(sorted_list, ans * 5)
        return ans


print(Solution().nthUglyNumber(10))
