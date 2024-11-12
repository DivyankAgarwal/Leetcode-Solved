class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # i = 0
        # j = 0
        # ans = []

        # while i < len(word1) and j < len(word2):
        #     ans.append(word1[i])
        #     ans.append(word2[j])

        #     i+=1
        #     j+=1
        
        # while i < len(word1):
        #     ans.append(word1[i])
        #     i+=1


        # while j < len(word2):
        #     ans.append(word2[j])
        #     j+=1

        # return ''.join(ans)

        
        even = 0
        odd = 1
        n = len(word1) + len(word2)
        ans = [''] * n


        for i in range(len(word1)):
            if even < n:
                ans[even] = word1[i]
                even +=2
            else:
                ans.append(word1[i])

        for i in range(len(word2)):
            if odd < n:
                ans[odd] = word2[i]
                odd +=2
            else:
                ans.append(word2[i])

        return  ''.join(ans)

        

        
        