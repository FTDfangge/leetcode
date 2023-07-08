# You are given an integer n, which indicates that there are n courses labeled 
# from 1 to n. You are also given an array relations where relations[i] = [
# prevCoursei, nextCoursei], representing a prerequisite relationship between course 
# prevCoursei and course nextCoursei: course prevCoursei has to be taken before course 
# nextCoursei. Also, you are given the integer k. 
# 
#  In one semester, you can take at most k courses as long as you have taken 
# all the prerequisites in the previous semesters for the courses you are taking. 
# 
#  Return the minimum number of semesters needed to take all courses. The 
# testcases will be generated such that it is possible to take every course. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
# Output: 3
# Explanation: The figure above represents the given graph.
# In the first semester, you can take courses 2 and 3.
# In the second semester, you can take course 1.
# In the third semester, you can take course 4.
#  
# 
#  Example 2: 
#  
#  
# Input: n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
# Output: 4
# Explanation: The figure above represents the given graph.
# In the first semester, you can only take courses 2 and 3 since you cannot 
# take more than two per semester.
# In the second semester, you can take course 4.
# In the third semester, you can take course 1.
# In the fourth semester, you can take course 5.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 15 
#  1 <= k <= n 
#  0 <= relations.length <= n * (n-1) / 2 
#  relations[i].length == 2 
#  1 <= prevCoursei, nextCoursei <= n 
#  prevCoursei != nextCoursei 
#  All the pairs [prevCoursei, nextCoursei] are unique. 
#  The given graph is a directed acyclic graph. 
#  
# 
#  Related Topics 位运算 图 动态规划 状态压缩 👍 189 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        pa = [[] for _ in range(n)]
        next_study = [i for i in range(n)]
        not_study = []
        for pre, to in relations:
            pa[to - 1].append(pre - 1)
            try:
                next_study.remove(to - 1)
                not_study.append(to - 1)
            except ValueError:
                pass
        num_of_study = 0
        num_of_semester = 0
        while True:
            num_of_semester += 1
            study = next_study.copy()
            num_of_study += study.__len__()
            # print("study: ", study)
            if num_of_study == n:
                return num_of_semester
            if not study:
                return -1
            next_study = []
            for i in study:
                for j in not_study.copy():
                    try:
                        pa[j].remove(i)
                        if not pa[j]:
                            next_study.append(j)
                            not_study.remove(j)
                    except ValueError:
                        pass
# leetcode submit region end(Prohibit modification and deletion)
