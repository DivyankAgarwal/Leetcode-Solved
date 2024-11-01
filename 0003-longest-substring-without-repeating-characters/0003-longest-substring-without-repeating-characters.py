class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = set()
        left = 0
    
        ans =0 

        for right in range(len(s)):
            if s[right] in checker:
                while s[right] in checker:
                    checker.remove(s[left])
                    left +=1

            checker.add(s[right])
            
            if right - left + 1 > ans:
                ans = (right-left+1)
        
        return ans