# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        ptr = head
        while ptr:
            stack.append(ptr)
            ptr = ptr.next
        i = 0
        j = len(stack) - 1
        while i < j:
            stack[i].next = stack[j]
            i += 1
            stack[j].next = stack[i]
            j -= 1
        stack[i].next = None
        