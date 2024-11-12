class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start = []
        end = []
        for s, e in intervals:
            start.append(s)
            end.append(e)

        start.sort()
        end.sort()
        rooms = 0

        end_ptr = 0

        for i in range(len(start)):
            if start[i] < end[end_ptr]:
                rooms+=1
            else:
                end_ptr+=1

        return rooms

            

        