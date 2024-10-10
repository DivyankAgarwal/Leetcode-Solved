class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
    
        # Min-Heap to store the sums and corresponding pairs
        min_heap = []
        
        
        for i in range(min(k, len(nums1))):  # No need to push more than k elements
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        result = []
        
       
        while k > 0 and min_heap:
            current_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # If there is a next element in nums2 for this pair, add the new pair to the heap
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
            
            k -= 1
        return result