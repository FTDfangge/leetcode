from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        def my_permutation(start: str, s: str) -> set:
            if s.__len__() == 1:
                return set(s)

            result = set()
            for idx, i in enumerate(s):
                temp = my_permutation(i, s[:idx] + s[idx + 1:])
                for t in temp:
                    result.add(i + t)
            return result

        ans = my_permutation('', s)
        return list(ans)


print(Solution().permutation('abc'))
