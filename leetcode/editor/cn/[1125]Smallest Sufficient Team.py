# In a project, you have a list of required skills req_skills, and a list of 
# people. The iᵗʰ person people[i] contains a list of skills that the person has. 
# 
#  Consider a sufficient team: a set of people such that for every required 
# skill in req_skills, there is at least one person in the team who has that skill. 
# We can represent these teams by the index of each person. 
# 
#  
#  For example, team = [0, 1, 3] represents the people with skills people[0], 
# people[1], and people[3]. 
#  
# 
#  Return any sufficient team of the smallest possible size, represented by the 
# index of each person. You may return the answer in any order. 
# 
#  It is guaranteed an answer exists. 
# 
#  
#  Example 1: 
#  Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],[
# "nodejs"],["nodejs","reactjs"]]
# Output: [0,2]
#  
#  Example 2: 
#  Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], 
# people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java",
# "csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# Output: [1,2]
#  
#  
#  Constraints: 
# 
#  
#  1 <= req_skills.length <= 16 
#  1 <= req_skills[i].length <= 16 
#  req_skills[i] consists of lowercase English letters. 
#  All the strings of req_skills are unique. 
#  1 <= people.length <= 60 
#  0 <= people[i].length <= 16 
#  1 <= people[i][j].length <= 16 
#  people[i][j] consists of lowercase English letters. 
#  All the strings of people[i] are unique. 
#  Every skill in people[i] is a skill in req_skills. 
#  It is guaranteed a sufficient team exists. 
#  
# 
#  Related Topics 位运算 数组 动态规划 状态压缩 👍 112 👎 0
import copy
import sys
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        int_skill = dict()
        requirement = 0
        for idx, s in enumerate(req_skills):
            int_skill[s] = 2 ** idx
            requirement |= 2 ** idx
        n = req_skills.__len__()
        dp = [None] * (2 ** n)
        dp[0] = []

        def get_people_skill(person: List[str]) -> int:
            personal_skill = 0
            for ss in person:
                personal_skill |= int_skill[ss]
            return personal_skill

        for i in range(people.__len__()):
            skill_i = get_people_skill(people[i])
            if skill_i == 0:
                continue
            for pre_skill in range(2 ** n):
                if dp[pre_skill] is None:
                    continue
                new = pre_skill | skill_i
                if not dp[new] or dp[new].__len__() > dp[pre_skill].__len__() + 1:
                    dp[new] = dp[pre_skill] + [i]

        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().smallestSufficientTeam(req_skills=["java", "nodejs", "reactjs"],
                                        people=[["java"], ["nodejs"], ["nodejs", "reactjs"]]))
print(Solution().smallestSufficientTeam(req_skills=["algorithms", "math", "java", "reactjs", "csharp",
                                                    "aws"], people=[["algorithms", "math", "java"],
                                                                    ["algorithms", "math", "reactjs"],
                                                                    ["java", "csharp", "aws"],
                                                                    ["reactjs", "csharp"],
                                                                    ["csharp", "math"], ["aws", "java"]]))
print(Solution().smallestSufficientTeam(["gvp", "jgpzzicdvgxlfix", "kqcrfwerywbwi", "jzukdzrfgvdbrunw", "k"],
                                        [[], [], [], [], ["jgpzzicdvgxlfix"], ["jgpzzicdvgxlfix", "k"],
                                         ["jgpzzicdvgxlfix", "kqcrfwerywbwi"], ["gvp"], ["jzukdzrfgvdbrunw"],
                                         ["gvp", "kqcrfwerywbwi"]]))
