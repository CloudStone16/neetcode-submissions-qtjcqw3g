# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        lower, upper = (list1, list2) if list1.val <= list2.val else (list2, list1)
        merged = lower
        ptr1 = lower.next
        ptr2 = upper
        while True:
            if not ptr1 and not ptr2:
                break
            if not ptr1:
                merged.next = ptr2
                break
            if not ptr2:
                merged.next = ptr1
                break
            else:
                if ptr1.val <= ptr2.val:
                    merged.next = ptr1
                    ptr1 = ptr1.next
                    merged = merged.next
                else:
                    merged.next = ptr2
                    ptr2 = ptr2.next
                    merged = merged.next
        return lower



