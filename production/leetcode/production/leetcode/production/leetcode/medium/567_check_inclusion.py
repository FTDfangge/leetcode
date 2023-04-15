class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_1 = dict()
        for i in s1:
            if i in dict_1:
                dict_1[i] += 1
            else:
                dict_1[i] = 1
        dict_2 = dict()

        def check() -> bool:
            for i in dict_1:
                if i in dict_2:
                    if dict_1[i] != dict_2[i]:
                        return False
                else:
                    return False
            return True

        if s2.__len__() < s1.__len__():
            return False

        for i in range(s1.__len__()):
            if s2[i] in dict_2:
                dict_2[s2[i]] += 1
            else:
                dict_2[s2[i]] = 1
        if check():
            return True
        for i in range(s2.__len__() - s1.__len__()):
            dict_2[s2[i]] -= 1
            if s2[i + s1.__len__()] in dict_2:
                dict_2[s2[i + s1.__len__()]] += 1
            else:
                dict_2[s2[i + s1.__len__()]] = 1
            if check():
                return True

        return False


print(Solution().checkInclusion(s1= "ab", s2 = "eidboaoo"))
