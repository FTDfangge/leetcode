from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors = list(set(divisors))
        score_dict = dict()
        for d in divisors:
            score_dict[d] = 0
        for i in nums:
            for d in divisors:
                if i % d == 0:
                    score_dict[d] += 1
        scores = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
        max_score = scores[0][1]
        anss = []
        for i in scores:
            if i[1] == max_score:
                anss.append(i[0])
            else:
                break
        anss.sort()
        return anss[0]


# print(Solution().maxDivScore(nums=[4, 7, 9, 3, 9], divisors=[5, 2, 3]))
# print(Solution().maxDivScore(nums=[20, 14, 21, 10], divisors=[5, 7, 5]))
# print(Solution().maxDivScore([63, 56, 92, 98, 34],
#                              [47, 91, 91, 23, 88, 43, 53, 29, 70, 23, 77, 24, 22, 4, 79, 38, 13, 36, 94, 19, 91, 44,
#                               8]))
print(Solution().maxDivScore([69, 3, 92, 14, 67, 90, 31, 40, 54, 63, 99, 88, 28, 100, 5, 72, 89, 60, 90, 71],
                             [97, 16, 7, 60, 6, 57, 73, 84, 17, 8, 77, 60, 7, 74, 74, 24, 52, 43, 94, 48, 9, 99]))
