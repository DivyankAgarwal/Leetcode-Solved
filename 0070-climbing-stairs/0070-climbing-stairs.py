class Solution:
    def climbStairs(self, n: int) -> int:

        #brute recursion TC:O(2^n)

        # if n == 0:
        #     return 1

        # if n == 1:
        #     return 1

        # one = self.climbStairs(n-1)
        # two = self.climbStairs(n-2)

        # return one+two

        #optimized

        # dp = [-1] * (n+1)

        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]

        #space optimized

        prev2 = 1
        prev1 = 1

        for i in range(2, n+1):
            cur = prev2+prev1

            prev2 = prev1
            prev1 = cur
        
        return prev1
        