# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        ind = c - n - 1
        if ind == -1:
            if head.next:
                return head.next
            return None
        node = head
        for i in range(0, ind):
            node = node.next
        node.next = node.next.next
        return head