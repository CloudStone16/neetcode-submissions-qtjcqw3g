# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        ptr1, ptr2 = l1, l2
        p1, p2 = 1, 1
        while ptr1:
            num1 = num1 + (p1 * ptr1.val)
            ptr1 = ptr1.next
            p1 = p1 * 10
        while ptr2:
            num2 = num2 + (ptr2.val * p2)
            p2 = p2 * 10
            ptr2 = ptr2.next
        res = num1 + num2
        node = ListNode(0, None)
        head = node
        while res > 0:
            val = res % 10
            res = res // 10
            node.val = val
            if res:
                node.next = ListNode(0, None)
                node = node.next
        return head