class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #brute  -recursive
        # def calculate(index, buy, cap):

        #     if cap == 0:
        #         return 0

        #     if index == n:
        #         return 0


        #     profit = 0
        #     if buy == 0:
        #         profit = max(0 + calculate(index+1, 0, cap), -1*prices[index] + calculate(index+1, 1, cap))


        #     elif buy == 1:
        #         profit = max(0 + calculate(index+1, 1, cap), prices[index] + calculate(index+1, 0, cap-1))


        #     return profit

        # n = len(prices)
        # return calculate(0, 0, 2)

        #memoization.

        def calculate(index, buy, cap,dp):
            if index == n or cap == 0:
                return 0

            if dp[index][buy][cap] != -1:
                return dp[index][buy][cap]

            if buy == 0:
                profit = max(0 + calculate(index+1, 0, cap,dp), -1*prices[index] + calculate(index+1, 1, cap,dp))



            elif buy == 1:
                profit = max(0 + calculate(index+1, 1, cap,dp), prices[index] + calculate(index+1, 0, cap-1,dp))


            dp[index][buy][cap] = profit

            return dp[index][buy][cap]

        n = len(prices)
        dp = [[[-1 for _ in range(3)]for _ in range(2)]for _ in range(n)]

    
        return calculate(0, 0, 2,dp)