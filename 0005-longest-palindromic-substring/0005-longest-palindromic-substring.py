class Solution:
    def longestPalindrome(self, s: str) -> str:

        #brute TC: O(n3)
        # def check(substring):
        #     return substring == substring[::-1]

        # longest = ''

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         substring = s[i:j+1]
        #         if check(substring) and len(substring) > len(longest):
        #             longest = substring

        
        # return longest
        
        #better

        result = ''

        resultlength = 0

        for i in range(len(s)):

            left,right = i,i
            #odd length
            while left >=0 and right < len(s) and s[left] == s[right]:
                if (right-left + 1) > resultlength:
                    result = s[left:right+1]
                    resultlength = (right-left+1)
                left -=1
                right +=1

            #even length
            left = i
            right = i+1

            while left >=0 and right < len(s) and s[left] == s[right]:
                if (right-left + 1) > resultlength:
                    result = s[left:right+1]
                    resultlength = (right-left+1)
                left -=1
                right +=1

        return result