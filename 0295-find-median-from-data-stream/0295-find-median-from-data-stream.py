#brute way

# class MedianFinder:

#     def __init__(self):
#         self.store = []
        

#     def addNum(self, num: int) -> None:
#         self.store.append(num)
        

#     def findMedian(self) -> float:
#         n = len(self.store)

#         self.store.sort()

#         if len(self.store) % 2 == 1:
#             return self.store[n // 2]

#         else:
#             mid1 = self.store[n // 2 - 1]
#             mid2 = self.store[n // 2]
#             return (mid1 + mid2) / 2

#better

class MedianFinder:

    def __init__(self):
        self.small_max_heap = []
        self.large_min_heap = []
        

    def addNum(self, num: int) -> None:

        #first insert into small heap
        heapq.heappush(self.small_max_heap, -num)

        #every num in small <= every num in large
        if self.small_max_heap and self.large_min_heap and -self.small_max_heap[0] > self.large_min_heap[0]:
            val = -1  * heapq.heappop(self.small_max_heap)
            heapq.heappush(self.large_min_heap, val)

        #uneven size

        if len(self.large_min_heap) > len(self.small_max_heap) + 1:
            val = heapq.heappop(self.large_min_heap)
            heapq.heappush(self.small_max_heap, -val)


        if len(self.small_max_heap) > len(self.large_min_heap) + 1:
            val = -heapq.heappop(self.small_max_heap)
            heapq.heappush(self.large_min_heap, val)

        
    def findMedian(self) -> float:

        if len(self.small_max_heap) > len(self.large_min_heap):
            return -self.small_max_heap[0]

        if len(self.small_max_heap) < len(self.large_min_heap):
            return self.large_min_heap[0]


        if len(self.small_max_heap) == len(self.large_min_heap):
            return ((-self.small_max_heap[0] +  self.large_min_heap[0]) / 2)
        
        
    

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()