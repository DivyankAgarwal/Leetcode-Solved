class MedianFinder:

    def __init__(self):
        self.store = []
        

    def addNum(self, num: int) -> None:
        self.store.append(num)
        

    def findMedian(self) -> float:
        n = len(self.store)

        self.store.sort()

        if len(self.store) % 2 == 1:
            return self.store[n // 2]

        else:
            mid1 = self.store[n // 2 - 1]
            mid2 = self.store[n // 2]
            return (mid1 + mid2) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()