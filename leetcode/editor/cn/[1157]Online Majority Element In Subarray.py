# Design a data structure that efficiently finds the majority element of a 
# given subarray. 
# 
#  The majority element of a subarray is an element that occurs threshold times 
# or more in the subarray. 
# 
#  Implementing the MajorityChecker class: 
# 
#  
#  MajorityChecker(int[] arr) Initializes the instance of the class with the 
# given array arr. 
#  int query(int left, int right, int threshold) returns the element in the 
# subarray arr[left...right] that occurs at least threshold times, or -1 if no such 
# element exists. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MajorityChecker", "query", "query", "query"]
# [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
# Output
# [null, 1, -1, 2]
# 
# Explanation
# MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
# majorityChecker.query(0, 5, 4); // return 1
# majorityChecker.query(0, 3, 3); // return -1
# majorityChecker.query(2, 3, 2); // return 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 2 * 10⁴ 
#  1 <= arr[i] <= 2 * 10⁴ 
#  0 <= left <= right < arr.length 
#  threshold <= right - left + 1 
#  2 * threshold > right - left + 1 
#  At most 10⁴ calls will be made to query. 
#  
# 
#  Related Topics 设计 树状数组 线段树 数组 二分查找 👍 107 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        arr = self.arr[left:right + 1]
        temp_dict = dict()
        visited = dict()
        for i in arr:
            try:
                temp_dict[i] += 1
                if temp_dict[i] >= threshold and i not in visited:
                    return i
            except KeyError:
                temp_dict[i] = 1
                if temp_dict[i] >= threshold and i not in visited:
                    visited[i] = True
                    return i
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# leetcode submit region end(Prohibit modification and deletion)
obj = MajorityChecker([1, 1, 2, 2, 1, 1])
queries = [[0, 5, 4], [0, 3, 3], [2, 3, 2]]
for q in queries:
    print(obj.query(*q))
