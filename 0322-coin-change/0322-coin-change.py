class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #brute recursive

        # def check(index,coins,amount):

        #     if index == 0:
        #         if amount % coins[0] == 0:
        #             return amount // coins[0]
        #         else:
        #             return float('inf')
            

        #     nonpick = 0 + check(index-1, coins, amount)

        #     pick = float('inf')

        #     if coins[index] <= amount:
        #         pick = 1 + check(index, coins, amount - coins[index])

        #     return min(pick, nonpick)


        # n = len(coins)
        # ans = check(n-1,coins,amount)

        # if ans >= float('inf'):
        #     return -1
        # else:
        #     return ans
        
        #mempoization

        '''
        Time Complexity:O(N*Target), as there are N*Target states therefore at max 
        ‘N*Target’ new problems will be solved.

        Space Complexity:O(N*Target) + O(N), the stack space will be O(N) and a 
        2D array of size N*T is used.
        
        '''

        def check(index,coins,amount,dp):

            if index == 0:
                if amount % coins[0] == 0:
                    return amount // coins[0]
                else:
                    return float('inf')

            if dp[index][amount] != -1:
                return dp[index][amount]
            

            nonpick = 0 + check(index-1, coins, amount,dp)

            pick = float('inf')

            if coins[index] <= amount:
                pick = 1 + check(index, coins, amount - coins[index],dp)

            dp[index][amount] = min(pick, nonpick)

            return dp[index][amount]

        
        
        n = len(coins)
        dp=[ [-1 for _ in range(amount + 1)] for _ in range(n)]

        ans = check(n-1,coins,amount,dp)

        if ans >= float('inf'):
            return -1
        else:
            return ans



