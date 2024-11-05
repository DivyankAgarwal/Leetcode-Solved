class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        n = len(str1)
        m = len(str2)

        dp = [[0 for _ in range(m+1)]for _ in range(n+1)]

        for ind1 in range(1, n+1):
            for ind2 in range(1, m+1):

                if str1[ind1-1] == str2[ind2 - 1]:
                    dp[ind1][ind2] = 1 +  dp[ind1-1][ind2-1]

                else:
                    dp[ind1][ind2] = max(dp[ind1-1][ind2], dp[ind1][ind2-1])

        
        lcs = dp[-1][-1]

        final_length = (n + m) - lcs

        print(final_length)
        print(dp)

        index = lcs 
        ans = []

        # Build the shortest supersequence by backtracking
        while n > 0 and m > 0:
            if str1[n - 1] == str2[m - 1]:
                ans.append(str1[n - 1])
                index -= 1
                n -= 1
                m -= 1
            elif dp[n - 1][m] > dp[n][m - 1]:
                ans.append(str1[n - 1])
                n -= 1
            else:
                ans.append(str2[m - 1])
                m -= 1

        # Add remaining characters from str1 or str2
        while n > 0:
            ans.append(str1[n - 1])
            n -= 1
        while m > 0:
            ans.append(str2[m - 1])
            m -= 1

        # Reverse the result since we built it backwards
        ans.reverse()
        return ''.join(ans)
        