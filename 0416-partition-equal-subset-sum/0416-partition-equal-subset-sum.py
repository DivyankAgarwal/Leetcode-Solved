class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        #recursive - brute
        # def check(index, target,nums):
        #     if target == 0:
        #         return True
            
        #     if index == 0:
        #         return nums[index] == target

        #     nonpick = check(index-1, target,nums)

        #     pick = False

        #     if target >= nums[index]:
        #         pick = check(index-1, target-nums[index], nums)


        #     return pick or nonpick
        


        # totalsum = 0
        # n = len(nums)
        # for i in nums:
        #     totalsum += i

        # if totalsum % 2 == 1:
        #     return False

        # else:
        #     k = totalsum // 2
        #     return check(n-1,k,nums)


        #memoization

        def check(index, target,nums,dp):
            if target == 0:
                return True

            if index == 0:
                return nums[index] == target

            #overlapping issue
            if dp[index][target] != -1:
                return dp[index][target] == 1

            
            nonpick = check(index-1, target,nums,dp)

            pick = False
            if target >= nums[index]:
                pick = check(index-1, target-nums[index],nums,dp)

            dp[index][target] = 1 if nonpick or pick else 0
            return dp[index][target] == 1



        totalsum = 0
        n = len(nums)
        for i in nums:
            totalsum += i

        if totalsum % 2 == 1:
            return False

        else:
            k = totalsum // 2
            dp = [ [-1 for _ in range(k+1)] for _ in range(n) ]
            return check(n-1,k,nums,dp)