class Solution:
    def jump(self, nums: List[int]) -> int:

        #brute TC: N**N; SC: O(N)

        # def jump_helper(index, jumps):
        #     if index >= len(nums) - 1:
        #         return jumps

        #     mini = float('inf')
        #     for i in range(1,nums[index]+1):
        #         mini = min(mini, jump_helper(index+i, jumps+1))
            
        #     return mini


        # return jump_helper(0,0)

        #Better TC: O(n**2)

        # n = len(nums)
        # dp = [float('inf')] * n  

        # dp[0] = 0  

        # for i in range(1, n):
        #     for j in range(i):

        #         if j + nums[j] >= i: 
        #             dp[i] = min(dp[i], dp[j] + 1)  

        # return dp[-1]  


        #Optimal O(N)

        n = len(nums)
    
        if n == 1:  
            return 0
        
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])  
            
       
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest  
                

                if current_jump_end >= n - 1:
                    break
        
        return jumps
        
        