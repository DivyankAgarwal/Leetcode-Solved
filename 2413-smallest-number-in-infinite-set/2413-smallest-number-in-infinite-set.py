class SmallestInfiniteSet:

    def __init__(self):
        self.pointer = 1
        self.min_heap = []
        self.set = set()
        

    def popSmallest(self) -> int:

        if self.min_heap:
            ele = heapq.heappop(self.min_heap)
            self.set.remove(ele)
            return ele
        else:
            current = self.pointer
            self.pointer+=1
            return current
        

    def addBack(self, num: int) -> None:

        if num < self.pointer and num not in self.min_heap:
            heapq.heappush(self.min_heap, num)
            self.set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)