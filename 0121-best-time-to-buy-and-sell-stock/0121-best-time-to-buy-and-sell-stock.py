class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #brute
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)
        
        # return max_profit

        #optimal

        # profit = 0

        # mini = float('inf')

        # for i in range(0, len(prices)):
        #     cost = prices[i] - mini

        #     profit = max(profit, cost)

        #     mini = min(mini, prices[i])

        
        # return profit
        max_profit = 0
        min_price = float('inf')

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            else:
                profit = prices[i] - min_price
                max_profit = max(max_profit, profit)
        
        return max_profit


        