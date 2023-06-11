# Given the head of a linked list, we repeatedly delete consecutive sequences 
# of nodes that sum to 0 until there are no such sequences. 
# 
#  After doing so, return the head of the final linked list. You may return any 
# such answer. 
# 
#  
#  (Note that in the examples below, all sequences are serializations of 
# ListNode objects.) 
# 
#  Example 1: 
# 
#  
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1,2,3,-3,-2]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The given linked list will contain between 1 and 1000 nodes. 
#  Each node in the linked list has -1000 <= node.val <= 1000. 
#  
# 
#  Related Topics 哈希表 链表 👍 244 👎 0
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        ptr = dummy.next
        pre_dict = dict()
        s = 0
        while ptr:
            s += ptr.val
            pre_dict[s] = ptr
            ptr = ptr.next
        ptr = dummy
        s = 0
        while ptr:
            s += ptr.val
            if s in pre_dict:
                ptr.next = pre_dict[s].next
            ptr = ptr.next
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)
head = ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1)))))
print(Solution().removeZeroSumSublists(head))
