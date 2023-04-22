class Solution:
    def addMinimum(self, word: str) -> int:
        ptr = 0
        temp_dict = dict()
        ans = 0
        while ptr in range(word.__len__()):
            if word[ptr] not in temp_dict and (
                    (word[ptr] == 'a' and not temp_dict) or
                    (word[ptr] == 'b' and 'c' not in temp_dict) or
                    (word[ptr] == 'c')):
                temp_dict[word[ptr]] = 1
            else:
                ans += 3 - (temp_dict.__len__())
                temp_dict = dict()
                temp_dict[word[ptr]] = 1
            ptr += 1
        ans += 3 - (temp_dict.__len__())
        return ans


# print(Solution().addMinimum(word="b"))
# print(Solution().addMinimum(word="aaa"))
print(Solution().addMinimum(word="aaaabb"))
print(Solution().addMinimum("aaaacb"))
