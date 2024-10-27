#using DLL

'''
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        #Left = LRU
        #Right = Most recently used
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    # 1 -> <- 2 -> <-3 = 1 -> <- 3

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    # 1-> <- 2 = 
    def insert(self, node):
        prev = self.right.prev
        next = self.right

        prev.next = next.prev = node

        node.next = next    
        node.prev = prev
        
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) >  self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
'''
#using dictionary
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()  
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move the accessed key to the end (mark as most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and mark as most recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        # If the cache exceeds capacity, remove the least recently used item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Pop from the beginning (LRU)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)