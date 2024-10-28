class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #brute
        '''
        Time Complexity:The time complexity is O(2^n) due to the recursive calls for each index.
        Space Complexity:The space complexity is O(n) due to the recursion stack.
        
        '''

        # def calculate(index):
        #     if index == 0:
        #         return nums[index]

        #     if index < 0:
        #         return 0

        #     pick = nums[index] + calculate(index - 2)

        #     nonpick = 0 + calculate(index -1)

        #     return max(pick, nonpick)


        # index = len(nums)-1
        # return calculate(index)


        #optimized tabulation

        n = len(nums)
        dp = [0] * n
        
        
        dp[0] = nums[0]

       
        for i in range(1, n):
            
           
            pick = nums[i]
            if i > 1:
                pick += dp[i - 2]
            nonPick = dp[i - 1]

           
            dp[i] = max(pick, nonPick)

       
        return dp[-1]