class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x : x[1])

        count = 0
        lastEnd = -float('inf')
        totalintervals = len(intervals)

        for start, end in intervals:
            if start >= lastEnd:
                count +=1
                lastEnd = end
        

        return totalintervals - count
        