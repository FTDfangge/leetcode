class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x < y:
            return (x * 2 + 1 + z) * 2
        elif x > y:
            return (y * 2 + 1 + z) * 2
        else:
            return (x * 2 + z) * 2

print(Solution().longestString())