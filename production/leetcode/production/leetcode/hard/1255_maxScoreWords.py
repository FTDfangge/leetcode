import copy
from typing import List


class Solution:
    def maxScoreWords2(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = words.__len__()
        all_possibilities = 2 ** n

        # construct letters dictionary
        letter_dict = dict()
        for l in letters:
            try:
                letter_dict[l] += 1
            except KeyError:
                letter_dict[l] = 1

        # construct word scores
        word_scores = []
        for w in words:
            temp_score = 0
            for ch in w:
                temp_score += score[ord(ch) - ord('a')]
            word_scores.append(temp_score)

        max_score = 0
        for i in range(all_possibilities):
            temp_score = 0
            combination = list(bin(i)[2:].zfill(n))
            word_letters = dict()
            for idx, c in enumerate(combination):
                if c != '0':
                    ww = words[idx]
                    temp_score += word_scores[idx]
                    for j in ww:
                        try:
                            word_letters[j] += 1
                        except KeyError:
                            word_letters[j] = 1
            # check could construct
            for item in word_letters.items():
                try:
                    if letter_dict[item[0]] < item[1]:  # could not construct
                        break
                except KeyError:
                    break
            else:  # could construct this possibility
                max_score = max(temp_score, max_score)
        return max_score

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_dict = dict()
        for l in letters:
            try:
                letter_dict[l] += 1
            except KeyError:
                letter_dict[l] = 1
        words_with_scores = []
        for idx, w in enumerate(words):
            temp_score = 0
            temp_letter_dict = dict()
            for i in w:
                temp_score += score[ord(i) - ord('a')]
                try:
                    temp_letter_dict[i] += 1
                except KeyError:
                    temp_letter_dict[i] = 1
            words_with_scores.append([temp_letter_dict, temp_score])

        def my_max_score(my_words: List[List], letters_dict: dict) -> int:
            max_score = 0
            for idx, (l_dict, my_score) in enumerate(my_words):
                # check could construct
                temp_l_dict = copy.deepcopy(letters_dict)

                for i in l_dict.items():
                    try:
                        temp_l_dict[i[0]] -= i[1]
                        if temp_l_dict[i[0]] < 0:
                            break
                    except KeyError:
                        break
                else:
                    max_score = max(max_score,
                                    my_score + my_max_score(my_words[:idx] + my_words[idx + 1:], temp_l_dict))

            return max_score

        return my_max_score(words_with_scores, letter_dict)


# print(
#     Solution().maxScoreWords(words=["dog", "cat", "dad", "good"], letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
#                              score=[1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                                     0]) == 23)
#
# print(Solution().maxScoreWords(words=["xxxz", "ax", "bx", "cx"], letters=["z", "a", "b", "c", "x", "x", "x"],
#                                score=[4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0,
#                                       10]) == 27)
#
# print(Solution().maxScoreWords(words=["leetcode"], letters=["l", "e", "t", "c", "o", "d"],
#                                score=[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
#                                       0]) == 0)

print(
    Solution().maxScoreWords2(words=["dog", "cat", "dad", "good"],
                              letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                              score=[1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0]) == 23)

print(Solution().maxScoreWords2(words=["xxxz", "ax", "bx", "cx"], letters=["z", "a", "b", "c", "x", "x", "x"],
                                score=[4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0,
                                       10]) == 27)

print(Solution().maxScoreWords2(words=["leetcode"], letters=["l", "e", "t", "c", "o", "d"],
                                score=[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                                       0]) == 0)
