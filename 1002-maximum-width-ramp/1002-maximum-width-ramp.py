class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        #brute
        # max_width = 0
    
      
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] <= nums[j]:  
        #             max_width = max(max_width, j - i)  
        
        # return max_width

        #better

        stack = []
    
       
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        print(nums)
        
        max_width = 0
        
       
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j - stack.pop())
        
        return max_width