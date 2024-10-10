import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        def calculate_dist(x1, x2):
            orix = 0
            oriy = 0

            ans = math.sqrt( (x1-orix)**2 + (x2 - oriy)**2 )

            return ans

        min_heap = []

        for i,point in enumerate(points):

            ans = calculate_dist(point[0],point[1])

            heapq.heappush(min_heap, [-ans,i])

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        print(min_heap)

        result = []

        while k > 0:
            index = min_heap[0][1]
            heapq.heappop(min_heap)
            result.append(points[index])
            k-=1

        return result




        