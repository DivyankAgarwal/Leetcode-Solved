class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        #recursive

        # def calculate(index, buy):
        #     if index == n:
        #         return 0

        #     profit = 0
        #     if buy == 0:
        #         profit = max(0+ calculate(index+1, 0), -1*prices[index]-fee + calculate(index+1, 1))


        #     elif buy == 1:
        #         profit = max(0 + calculate(index+1, 1), prices[index] + calculate(index+1, 0))



        #     return profit



        # n = len(prices)
        # return calculate(0, 0)
        

        #memoization

        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n)]


        def calculate(index,buy,dp):
            if index == n:
                return 0

            if dp[index][buy] != -1:
                return dp[index][buy]


            if buy == 0:
                profit = max(0+ calculate(index+1, 0,dp), -1*prices[index]-fee + calculate(index+1, 1,dp))




            elif buy == 1:
                profit = max(0 + calculate(index+1, 1,dp), prices[index] + calculate(index+1, 0,dp))

        

            dp[index][buy] = profit
            return dp[index][buy]

        return calculate(0, 0,dp)
