# You are given an integer n, which indicates that there are n courses labeled 
# from 1 to n. You are also given an array relations where relations[i] = [
# prevCoursei, nextCoursei], representing a prerequisite relationship between course 
# prevCoursei and course nextCoursei: course prevCoursei has to be taken before course 
# nextCoursei. 
# 
#  In one semester, you can take any number of courses as long as you have 
# taken all the prerequisites in the previous semester for the courses you are taking. 
# 
# 
#  Return the minimum number of semesters needed to take all courses. If there 
# is no way to take all the courses, return -1. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 3, relations = [[1,3],[2,3]]
# Output: 2
# Explanation: The figure above represents the given graph.
# In the first semester, you can take courses 1 and 2.
# In the second semester, you can take course 3.
#  
# 
#  Example 2: 
#  
#  
# Input: n = 3, relations = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: No course can be studied because they are prerequisites of each 
# other.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 5000 
#  1 <= relations.length <= 5000 
#  relations[i].length == 2 
#  1 <= prevCoursei, nextCoursei <= n 
#  prevCoursei != nextCoursei 
#  All the pairs [prevCoursei, nextCoursei] are unique. 
#  
# 
#  Related Topics 图 拓扑排序 👍 62 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
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
print(Solution().minimumSemesters(n=3, relations=[[1, 3], [2, 3]]))
