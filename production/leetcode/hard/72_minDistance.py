class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a_len = word1.__len__() + 1
        b_len = word2.__len__() + 1
        dp = [[0] * b_len for _ in range(a_len)]
        # init dp
        for i in range(a_len):
            dp[i][0] = i
        for j in range(b_len):
            dp[0][j] = j

        # do dp
        for i in range(1, a_len):
            for j in range(1, b_len):
                insert_a = dp[i][j - 1] + 1
                insert_b = dp[i - 1][j] + 1
                replace = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    replace += 1
                dp[i][j] = min(insert_a, insert_b, replace)
        return dp[a_len - 1][b_len - 1]


print(Solution().minDistance(word1="horse", word2="ros"))
print(Solution().minDistance(word1="intention", word2="execution"))
