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

        # def check(index, target,nums,dp):
        #     if target == 0:
        #         return True

        #     if index == 0:
        #         return nums[index] == target

        #     #overlapping issue
        #     if dp[index][target] != -1:
        #         return dp[index][target]

            
        #     nonpick = check(index-1, target,nums,dp)

        #     pick = False
        #     if target >= nums[index]:
        #         pick = check(index-1, target-nums[index],nums,dp)

            
        #     dp[index][target] = pick or nonpick
        #     return dp[index][target]



        # totalsum = 0
        # n = len(nums)
        # for i in nums:
        #     totalsum += i

        # if totalsum % 2 == 1:
        #     return False

        # else:
        #     k = totalsum // 2
        #     dp = [ [-1 for _ in range(k+1)] for _ in range(n) ]
        #     return check(n-1,k,nums,dp)

        #tabulation

        def check(index, target, nums, dp):
            #base case if target == 0 for every index
            for i in range(len(nums)):
                dp[i][0] = 1


            #2nd base case. if index == 0 and target is at index == 0
            if target >= nums[0]:
                dp[0][nums[0]] = 1
            

            for ind in range(1, index+1):
                for tar in range(1, target+1):

                    nonpick = dp[ind-1][tar]

                    pick = False

                    if tar >= nums[ind]:
                        pick = dp[ind-1][tar-nums[ind]]


                    dp[ind][tar] = nonpick or pick

            return dp[index][target] == 1

        totalsum = 0
        n = len(nums)
        for i in nums:
            totalsum += i

        if totalsum % 2 == 1:
            return False

        else:
            k = totalsum // 2
            dp = [ [0 for _ in range(k+1)] for _ in range(n) ]
            return check(n-1,k,nums,dp)

