import sys


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start = 0
        # init window
        white_count = 0
        for i in range(k - 1):
            if blocks[i] == 'W':
                white_count += 1
        end = k - 1
        min_white_count = sys.maxsize
        while end < blocks.__len__():
            white_count += 1 if blocks[end] == 'W' else 0
            min_white_count = min(min_white_count, white_count)
            white_count -= 1 if blocks[start] == 'W' else 0
            start += 1
            end += 1
        return min_white_count


print(Solution().minimumRecolors(blocks="WBBWWBBWBW", k=7))
print(Solution().minimumRecolors(blocks="WBWBBBW", k=2))
