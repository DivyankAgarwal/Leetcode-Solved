class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #brute recursive

        # def check(index,coins,amount):

        #     if index == 0:
        #         if amount % coins[0] == 0:
        #             return 1
        #         else:
        #             return 0
            

        #     nonpick = 0 + check(index-1, coins, amount)

        #     pick = 0

        #     if coins[index] <= amount:
        #         pick = check(index, coins, amount - coins[index])

        #     return pick + nonpick


        # n = len(coins)
        # return check(n-1,coins,amount)

        #memoization

        # def check(index, coins,amount, dp):

        #     if index == 0:
        #         if amount % coins[0] == 0:
        #             return 1

        #         else:
        #             return 0

        #     nonpick = 0 + check(index-1,coins,amount,dp)

        #     pick = 0

        #     if coins[index] <= amount:
        #         pick = check(index,coins,amount - coins[index],dp)


        #     return pick + nonpick

        # n = len(coins)
        # dp = [[-1 for _ in range(amount+1)]for _ in range(n)]
        # return check(n-1,coins,amount, dp)


        #tabulation

        n = len(coins)
        dp = [[0 for _ in range(amount+1)]for _ in range(n)]

        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = 1

        for index in range(1, n):
            for target in range(amount+1):

                nonpick = 0 + dp[index-1][target]

                pick = 0

                if coins[index] <= target:
                    pick = dp[index][target - coins[index]]


                dp[index][target] = pick + nonpick

        return dp[-1][amount]
