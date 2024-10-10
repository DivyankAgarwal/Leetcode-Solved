import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        #brute
        # nums.sort(reverse=True)

        # return nums[k-1]


        #optimal
        min_heap = []
        
        for n in nums:
            heapq.heappush(min_heap, n)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        
        return min_heap[0]

        