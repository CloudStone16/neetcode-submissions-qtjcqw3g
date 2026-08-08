class LRUCache:

    class Node:
        def __init__(self, key, val, next = None, prev = None):
            self.key = key
            self.val = val
            self.next = next
            self.previous = prev

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.tail = self.head = None
    
    def moveToFront(self, node):
        if node == self.head:
            return
        if self.head == self.tail == None:
            self.head = self.tail = node
            return
        
        if node.next == node.previous == None:
            node.next = self.head
            self.head.previous = node
            self.head = node
            return

        if node == self.tail:
            self.tail = node.previous
            node.previous.next = None
            node.previous = None
            node.next = self.head
            self.head.previous = node
            self.head = node
            return

        else:
            node.previous.next = node.next
            node.next.previous = node.previous
            node.next = self.head
            node.previous = None
            self.head.previous = node
            self.head = node
            return
    
    def removeTail(self):
        if not self.tail:
            return

        if self.head == self.tail:
            del self.cache[self.tail.key]
            self.head = self.tail = None
            return

        else:
            self.tail.previous.next = None
            del self.cache[self.tail.key]
            self.tail = self.tail.previous
            return


    def get(self, key: int) -> int:
        if key in self.cache:
            self.moveToFront(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.moveToFront(self.cache[key])
            return
        elif len(self.cache) < self.capacity:
            node = self.Node(key, value)
            self.cache[key] = node
            self.moveToFront(node)
            return
        else:
            self.removeTail()
            node = self.Node(key, value)
            self.cache[key] = node
            self.moveToFront(node)
            return
