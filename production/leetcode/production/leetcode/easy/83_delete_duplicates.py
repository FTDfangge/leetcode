from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new_head = ListNode(head.val)
        ptr = head.next
        new_ptr = new_head
        while ptr:
            if ptr.val > new_ptr.val:
                new_ptr.next = ListNode(ptr.val)
                new_ptr = new_ptr.next
            ptr = ptr.next
        return new_head
