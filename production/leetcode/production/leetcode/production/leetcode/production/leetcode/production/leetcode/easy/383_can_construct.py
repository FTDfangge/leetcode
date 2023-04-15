class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if magazine.__len__() < ransomNote.__len__():
            return False
        ransom_dict = dict()
        for i in ransomNote:
            if i in ransom_dict:
                ransom_dict[i] += 1
            else:
                ransom_dict[i] = 1
        magazine_dict = dict()
        for i in magazine:
            if i in magazine_dict:
                magazine_dict[i] += 1
            else:
                magazine_dict[i] = 1
        for i in ransom_dict:
            if i not in magazine_dict:
                return False
            else:
                if magazine_dict[i] < ransom_dict[i]:
                    return False
        return True


print(Solution().canConstruct(ransomNote="aa", magazine="aab"))
