class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        '''
        The main objective is to determine how many meetings are ongoing at any point in 
        time to understand the peak room usage. We don’t actually need to know which specific 
        start time pairs with which end time. Instead, we simply need to know:

        When each meeting begins.
        When each meeting ends.
        
        '''

        # start = []
        # end = []
        # for s, e in intervals:
        #     start.append(s)
        #     end.append(e)

        # start.sort()
        # end.sort()
        # rooms = 0

        # end_ptr = 0

        # for i in range(len(start)):
        #     if start[i] < end[end_ptr]:
        #         rooms+=1
        #     else:
        #         end_ptr+=1

        # return rooms

        #using min_heap

        if not intervals:
            return 0

       
        intervals.sort(key=lambda x: x[0])

        
        min_heap = []
        heapq.heappush(min_heap, intervals[0][1])  

       
        for i in range(1, len(intervals)):
           
            if min_heap[0] <= intervals[i][0]:
                heapq.heappop(min_heap)  

            # Add the current meeting's end time to the heap
            heapq.heappush(min_heap, intervals[i][1])

        
        return len(min_heap)

            

        