class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #brute recursive


        # def check(index,buy):
        #     if index >= n:
        #         return 0

        #     profit = 0

        #     if buy == 0:
        #         profit = max(0 + check(index+1, 0), -1*prices[index] + check(index+1, 1))

        #     elif buy == 1:
        #         profit = max(0 + check(index+1, 1), prices[index] + check(index+2, 0))

            
        #     return profit



        # n = len(prices)
        # return check(0, 0)

        #memoization
        
        n = len(prices)
        dp = [[-1 for _ in range(2)]for _ in range(n)]

        def check(index, buy, dp):
            if index >= n:
                return 0


            if dp[index][buy] != -1:
                return dp[index][buy]

            profit = 0
            if buy == 0:
                profit = max(0 + check(index+1, 0,dp), -1*prices[index] + check(index+1, 1,dp))


            elif buy == 1:
                profit = max(0 + check(index+1, 1,dp), prices[index] + check(index+2, 0,dp))



            dp[index][buy] = profit

            return dp[index][buy]


        return check(0,0,dp)
        