# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        newHead = ListNode()
        c = 0
        nhead = head
        while nhead:
            dummy.next, ctail, nhead = self.reverseGroup(nhead, k)
            if c == 0:
                newHead = dummy.next
                c += 1
            dummy = ctail
        
        return newHead



    def isValidGroup(self, node, k):
        if not node:
            return False
        c = 0
        while c < k and node:
            node = node.next
            c += 1
        return c == k
        
    def reverseGroup(self, node, k):
        flag = self.isValidGroup(node, k)
        if not flag:
            return node, node, None
        else:
            tail = node
            c = 0
            prev = None
            ptr = node
            while ptr and c < k:
                nextp = ptr.next
                ptr.next = prev
                prev = ptr 
                ptr = nextp
                c += 1
        
        return prev, tail, ptr
                