class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        #recursive 
        '''
        Time Complexity: O(2N+M), Where N is the length of the given string.

        Space Complexity:O(N+M), As we are using a recursion stack space(O(N+M)).
         
        '''
        # def find(index1, index2,text1, text2):
        #     if index1 < 0 or index2 < 0:
        #         return 0

        #     if text1[index1] == text2[index2]:
        #         return 1 + find(index1-1, index2-1, text1, text2)

        #     else:
        #         return max(find(index1-1, index2, text1, text2), find(index1, index2-1, text1, text2))



        # n = len(text1)
        # m = len(text2)

        # return find(n-1,m-1, text1, text2)

        #memoization

        # def find(index1, index2, text1, text2,dp):
        #     if index1 < 0 or index2 < 0:
        #         return 0


        #     if text1[index1] == text2[index2]:
        #         dp[index1][index2] =  1 + find(index1-1, index2-1, text1, text2,dp)

        #     else:
        #         dp[index1][index2] =  max(find(index1-1, index2, text1, text2,dp),find(index1, index2-1, text1, text2, dp))

        #     return dp[index1][index2]
        # n = len(text1)
        # m = len(text2)

        # dp = [[-1 for _ in range(m)]for _ in range(n)]

        # return find(n-1,m-1, text1, text2,dp)

        #tabulation.

        n = len(text1)
        m = len(text2)
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Initialize the base cases
        for i in range(n + 1):
            dp[i][0] = 0
        for i in range(m + 1):
            dp[0][i] = 0

        
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                
                
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
        
       
        return dp[n][m]

        