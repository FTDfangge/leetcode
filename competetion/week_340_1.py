import math
from typing import List


def check_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        max_prime = 0
        for i in range(nums.__len__()):
            if check_prime(nums[i][i]):
                max_prime = max(max_prime, nums[i][i])
            if check_prime(nums[i][nums.__len__() - i - 1]):
                max_prime = max(max_prime, nums[i][nums.__len__() - i - 1])
        return max_prime


print(Solution().diagonalPrime(nums=[[1, 2, 3], [5, 6, 7], [9, 10, 11]]))
print(Solution().diagonalPrime(nums=[[1, 2, 3], [5, 17, 7], [9, 11, 10]]))
for i in range(100):
    print(i, check_prime(i))
