class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
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
        dp = [[[-1 for _ in range(k+1)]for _ in range(2)]for _ in range(n)]

    
        return calculate(0, 0, k,dp)
        