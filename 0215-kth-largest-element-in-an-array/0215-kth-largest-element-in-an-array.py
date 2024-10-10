import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        #brute
        nums.sort(reverse=True)

        return nums[k-1]

        