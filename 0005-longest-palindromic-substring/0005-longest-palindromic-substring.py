class Solution:
    def longestPalindrome(self, s: str) -> str:

        #brute
        def check(substring):
            return substring == substring[::-1]

        longest = ''

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if check(substring) and len(substring) > len(longest):
                    longest = substring

        
        return longest
        