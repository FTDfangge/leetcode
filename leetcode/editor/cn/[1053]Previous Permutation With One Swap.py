# Given an array of positive integers arr (not necessarily distinct), return 
# the lexicographically largest permutation that is smaller than arr, that can be 
# made with exactly one swap. If it cannot be done, then return the same array. 
# 
#  Note that a swap exchanges the positions of two numbers arr[i] and arr[j] 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [3,2,1]
# Output: [3,1,2]
# Explanation: Swapping 2 and 1.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [1,1,5]
# Output: [1,1,5]
# Explanation: This is already the smallest permutation.
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [1,9,4,6,7]
# Output: [1,7,4,6,9]
# Explanation: Swapping 9 and 7.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 10⁴ 
#  1 <= arr[i] <= 10⁴ 
#  
# 
#  Related Topics 贪心 数组 👍 51 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        pre = arr[-1]
        for i in range(arr.__len__() - 2, -1, -1):
            if arr[i] <= pre:
                pre = arr[i]
            else:
                break
        else:
            return arr

        largest = 0
        largest_index = 0
        for j in range(i+1, arr.__len__()):
            if arr[j] < arr[i]:
                if arr[j] > largest:
                    largest = max(largest, arr[j])
                    largest_index = j
        temp = arr[i]
        arr[i] = largest
        arr[largest_index] = temp
        return arr


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().prevPermOpt1(arr=[3, 2, 1]))
print(Solution().prevPermOpt1(arr=[1, 1, 5]))
print(Solution().prevPermOpt1(arr=[1, 9, 4, 6, 7]))
print(Solution().prevPermOpt1(arr=[3, 1, 1, 3]))
