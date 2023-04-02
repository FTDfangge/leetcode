# 给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 
# secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。 
# 
#  返回这 两个区间列表的交集 。 
# 
#  形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。 
# 
#  两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,
# 24],[25,26]]
# 输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#  
# 
#  示例 2： 
# 
#  
# 输入：firstList = [[1,3],[5,9]], secondList = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：firstList = [], secondList = [[4,8],[10,12]]
# 输出：[]
#  
# 
#  示例 4： 
# 
#  
# 输入：firstList = [[1,7]], secondList = [[3,10]]
# 输出：[[3,7]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= firstList.length, secondList.length <= 1000 
#  firstList.length + secondList.length >= 1 
#  0 <= starti < endi <= 10⁹ 
#  endi < starti+1 
#  0 <= startj < endj <= 10⁹ 
#  endj < startj+1 
#  
# 
#  Related Topics 数组 双指针 👍 369 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr1 = 0
        ptr2 = 0
        intersection = []
        while ptr1 in range(firstList.__len__()) and ptr2 in range(secondList.__len__()):
            left1, right1 = firstList[ptr1]
            left2, right2 = secondList[ptr2]
            # get intersection
            l = max(left1, left2)
            r = min(right1, right2)
            if l <= r:
                intersection.append([l, r])
            if right1 <= right2:
                ptr1 += 1
            else:
                ptr2 += 1
        return intersection


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                                      secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))
