from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        max_num = 10 ** n - 1
        return [i + 1 for i in range(max_num)]
