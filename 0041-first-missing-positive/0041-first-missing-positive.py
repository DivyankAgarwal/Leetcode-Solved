class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        #brute
        # smp = 1
        # nums.sort()  #(n log n)
        # n = len(nums)

        # for i in range(n):
        #     if nums[i] == smp:
        #         smp+=1
        
        # return smp


        # Optimal

        # smp = 1
        # if len(nums) == 0:
        #     return smp


        # i = 0
        # j = len(nums) - 1

        # while i<=j:


        #     if nums[i] == smp:
        #         smp+=1
        #         i+=1
        #     elif nums[j] == smp:
        #         smp+=1
        #         j-=1

        #     elif nums[i] < smp:
        #         i+=1

        #     elif nums[j] < smp:
        #         j-=1

        #     else:
        #         if nums[i] > len(nums):
        #             i += 1
        #         elif nums[j] > len(nums):
        #             j -= 1
        #         else:
        #             i += 1

        # return smp
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]


        for i in range(n):
            if nums[i] != i+1:
                return i+1


        return n+1
