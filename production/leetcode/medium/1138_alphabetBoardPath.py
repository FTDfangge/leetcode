import copy


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        alpha_dict = {}
        for i in range(26):
            alpha_dict[chr(i + ord('a'))] = [i // 5, i % 5]
        ans = ''
        position = [0, 0]
        for i in target:
            i_pos = alpha_dict[i]
            if position[0] == 5:
                if position[0] <= i_pos[0]:
                    ans += 'D' * (i_pos[0] - position[0])
                else:
                    ans += 'U' * (position[0] - i_pos[0])
                if position[1] <= i_pos[1]:
                    ans += 'R' * (i_pos[1] - position[1])
                else:
                    ans += 'L' * (position[1] - i_pos[1])
            else:
                if position[1] <= i_pos[1]:
                    ans += 'R' * (i_pos[1] - position[1])
                else:
                    ans += 'L' * (position[1] - i_pos[1])

                if position[0] <= i_pos[0]:
                    ans += 'D' * (i_pos[0] - position[0])
                else:
                    ans += 'U' * (position[0] - i_pos[0])
            ans += '!'
            position = copy.deepcopy(i_pos)
        return ans


print(Solution().alphabetBoardPath('leet'))
print(Solution().alphabetBoardPath('code'))
