class Solution:
    def rob(self, nums: List[int]) -> int:
        #brute
        # def check(index,arr):
        #     if index == 0:
        #         return arr[index]

        #     if index < 0:
        #         return 0


        #     pick = arr[index] + check(index-2,arr)
        #     non_pick = 0 + check(index-1,arr)

        #     return max(pick, non_pick)

        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]

        # arr1 = []
        # arr2 = []
        # n = len(nums) - 1
        # for i in range(len(nums)):
        #     if i != n:
        #         arr1.append(nums[i])

        #     if i!= 0:
        #         arr2.append(nums[i])

        # m = len(arr1) - 1
        # ans1 = check(m,arr1)
        # ans2 = check(m,arr2)

        # return max(ans1,ans2)
        
        #better - tabulation
        n = len(nums)
        if n < 0:
            return 0
        if n == 1:
            return nums[0]
        
        arr1 = nums[1:]
        arr2 = nums[:-1]

        dp1 = [0] * len(arr1)
        dp2 = [0] * len(arr2)

        dp1[0] = arr1[0]
        dp2[0] = arr2[0]

        for i in range(1, len(arr1)):


            pick1 = arr1[i]
            pick2 = arr2[i]
            if i > 1:
                pick1 += dp1[i-2]
                pick2 += dp2[i-2]

            nonpick1 = dp1[i-1]
            nonpick2 = dp2[i-1]

            dp1[i] = max(pick1,nonpick1)
            dp2[i] = max(pick2,nonpick2)

        return max(dp1[-1],dp2[-1])
