class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # def check(index, target):
        #     if target == 0:
        #         return 1

        #     if index == 0:
        #         if target == 0 and target == nums[0]: #1+1:
        #             return 2
        #         if target == nums[0]:
        #             return 1


        #     nonpick = 0 + check(index-1, target)

        #     pick = 0
        #     if nums[index] <= target:
        #         pick = check(index-1, target - nums[index])

        #     return pick+nonpick

        # n = len(nums)
        # total = sum(nums)
        # new_target = (total - target)// 2
        # return check(n-1, new_target)

        #memoization

        def check(index, target,dp):

            if index == 0:
                if target == 0 and nums[0] == target:
                    return 2


                if target == 0 or nums[0] == target:
                    return 1
                return 0


            if dp[index][target] != -1:
                return dp[index][target]


            nonpick = 0 + check(index-1, target, dp)

            pick = 0
            if nums[index] <= target:
                pick = check(index-1, target-nums[index],dp)


            dp[index][target] = pick +  nonpick

            return dp[index][target]

        n = len(nums)
        total = sum(nums)


        if total - target < 0 or (total - target )% 2 == 1:
            return 0

        new_target = (total - target)// 2
        dp = [[-1 for _ in range(new_target+1)] for _ in range(n)]


        return check(n-1, new_target,dp)



        