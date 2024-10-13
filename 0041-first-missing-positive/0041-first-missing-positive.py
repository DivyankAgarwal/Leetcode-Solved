class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        #brute
        smp = 1
        nums.sort()  #(n log n)
        n = len(nums)

        for i in range(n):
            if nums[i] == smp:
                smp+=1
        
        return smp


        # Optimal
        