class Solution:
    def countBits(self, n: int) -> List[int]:


        #Brute TC: O(n log n)
        # result = []

        # for i in range(n+1):
        #     count = 0

        #     while i > 0:
        #         count+= i & 1
        #         i = i >> 1
        #     result.append(count)
        
        # return result


        #Optimal TC: O(n)
        
        result = [0] * (n + 1)
        
        
        for i in range(1, n + 1):
            
            result[i] = result[i >> 1] + (i & 1)
        
        return result