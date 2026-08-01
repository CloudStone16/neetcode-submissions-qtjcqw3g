"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}
        ptr = head
        if not head:
            return None
        while ptr:
            node = Node(ptr.val, None, None)
            map[ptr] = node
            ptr = ptr.next
        for n in map:
            if n.next:
                map[n].next = map[n.next]
            if n.random:
                map[n].random = map[n.random]

        return map[head]