# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        start = slow.next
        slow.next = None
        ptr2 = self.reverse(start)
        ptr1 = head
        
        while ptr2:
            tmp1, tmp2 = ptr1.next, ptr2.next
            ptr1.next = ptr2
            ptr1 = tmp1
            ptr2.next = ptr1
            ptr2 = tmp2

    def reverse(self, head) -> ListNode:
        current = head
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous
        