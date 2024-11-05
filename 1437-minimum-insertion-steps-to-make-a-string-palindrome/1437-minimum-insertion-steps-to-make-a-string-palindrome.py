class Solution:
    def minInsertions(self, s: str) -> int:

        if s == s[::-1]:
            return 0

        def find():
            n = len(s)
            s2 = s[::-1]

            dp = [[0 for _ in range(n+1)]for _ in range(n+1)]

            for ind1 in range(1, n+1):
                for ind2 in range(1, n+1):
                    if s[ind1-1] == s2[ind2 - 1]:
                        dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]

                    else:
                        dp[ind1][ind2] = max(dp[ind1-1][ind2], dp[ind1][ind2-1])

            return dp[n][n]
        
        count = find()

        return len(s) - count


        