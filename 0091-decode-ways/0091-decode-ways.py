class Solution:
    def numDecodings(self, s: str) -> int:
        #brute recursive

        # def count_ways(index):
     
        #     if index == len(s):
        #         return 1
            
        #     if s[index] == '0':
        #         return 0

        #     result = 0
            
        #     # Recursive calls based on valid possibilities
        #     # Possibility 1: Single-digit decode
        #     result += count_ways(index + 1)

        #     # Possibility 2: Two-digit decode (if valid)
        #     if index + 1 < len(s) and 10 <= int(s[index:index + 2]) <= 26:
        #         result += count_ways(index + 2)
            
        #     return result
        
        # return count_ways(0)


        #memoization
        n =len(s)
        dp = [-1 for _ in range(len(s))] 

        def count_ways(index,dp):
            if index == n:
                return 1

            if s[index] == '0':
                return 0

            if dp[index] != -1:
                return dp[index]

            result = 0

            result += count_ways(index+1,dp)


            if index+2 <= len(s) and 10<= int(s[index:index+2])<=26:
                result += count_ways(index+2,dp)

            
            dp[index] = result

            return dp[index]



        return count_ways(0,dp)