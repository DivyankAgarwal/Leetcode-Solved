class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #brute TC: O(2^n)
        # def check(index, buy):
        #     if index == n:
        #         return 0

        #     profit = 0

        #     if buy == 0:
        #         profit = max( -1*prices[index] + check(index+1,1) , 0 + check(index+1, 0) )
                
        #     elif buy == 1: 
        #         profit = max( prices[index] + check(index+1,0) , 0 + check(index+1, 1) )

        #     return profit



        # n = len(prices)
        # return check(0,0)

        #memoization
        n = len(prices)
        dp = [[-1 for _ in range(2) ] for _ in range(n)]
        
        def check(index, buy):
            if index == n:
                return 0

            if dp[index][buy] != -1:
                return dp[index][buy]
            profit = 0

            if buy == 0:
                profit = max( 0 + check( index+1,0 ), -1*prices[index] + check( index+1,1 ) )

            elif buy == 1:
                profit = max( 0 + check(index+1, 1 ), prices[index] + check(index+1, 0 ) )


            dp[index][buy] = profit

            return dp[index][buy]


        ans = check(0,0)
        return ans
        