# Given a linked list, swap every two adjacent nodes and return its head. You 
# must solve the problem without modifying the values in the list's nodes (i.e., 
# only nodes themselves may be changed.) 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#  
# 
#  Example 2: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 100]. 
#  0 <= Node.val <= 100 
#  
# 
#  Related Topics 递归 链表 👍 1930 👎 0
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        pre = dummy
        ptr = head
        while True:
            if not ptr:
                return dummy.next
            elif not ptr.next:
                pre.next = ptr
                return dummy.next
            else:
                temp = ptr.next.next
                ptr.next.next = ptr
                pre.next = ptr.next
                pre = ptr
                ptr.next = temp
                ptr = ptr.next


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
