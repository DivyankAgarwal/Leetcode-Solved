class Solution:
    def findLongestChain(self, data: List[List[int]]) -> int:

        pairs = []

        for i in range(len(data)):
            pairs.append([data[i][0], data[i][1]])

        #sort on end time asc

        pairs.sort(key = lambda x : x[1])

        lastEnd = -float('inf')
        count = 0

        for i in range(len(pairs)):

            if pairs[i][0] > lastEnd:
                lastEnd = pairs[i][1]
                count+=1
        
        return count
        