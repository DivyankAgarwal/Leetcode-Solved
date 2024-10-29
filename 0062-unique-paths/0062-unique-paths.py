class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #brute recursive
        # def getPath(m,n):
        #     if m == 0 and n == 0:
        #         return 1

        #     if m < 0 or n < 0:
        #         return 0

        #     up = getPath(m-1, n)
        #     down = getPath(m, n-1)

        #     return up+down


        # return getPath(m-1,n-1)

        #tabulation
        dp = [[0 for _ in range(n) ] for _ in range(m)]

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue

                up = 0
                down = 0

                if i > 0:
                    up = dp[i-1][j]

                if j > 0:
                    down = dp[i][j-1]

                dp[i][j] = up + down

        return dp[-1][-1]
        
        