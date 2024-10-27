class Solution:
    def countSubstrings(self, s: str) -> int:

        #brute

        def check_if_palindrome(s):
            return s == s[::-1]

        count = 0
        n = len(s)

        for i in range(n):
            for j in range(i,n):
                if check_if_palindrome(s[i:j+1]):
                    count+=1


        return count
        