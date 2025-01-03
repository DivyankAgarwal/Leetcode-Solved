class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])


        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = ans[-1]
            current = intervals[i]

            if prev[1] >= current[0]:
                prev[1] = max(prev[1], current[1])
            else:
                ans.append(current)
        
        return ans

        