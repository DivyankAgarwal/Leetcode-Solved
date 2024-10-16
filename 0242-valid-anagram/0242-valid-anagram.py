class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #brute

        # s = ''.join(sorted(s))

        # t = ''.join(sorted(t))
        

        # return s == t

        #Optimal

        freqS = [0] * 26
        freqT = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            freqS[ord(s[i]) - ord('a')] +=1
            freqT[ord(t[i]) - ord('a')] +=1

        print(freqS)
        print(freqT)

        for i in range(26):
            if freqS[i] != freqT[i]:
                return False
        return True
        