import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #brute

        
        # points_with_distances = [(point[0]**2 + point[1]**2, point) for point in points]
        
        # points_with_distances.sort(key=lambda x: x[0])
        
        # result = [point for _, point in points_with_distances[:k]]
        
        # return result


        #better
        def calculate_dist(x1, x2):
            orix = 0
            oriy = 0

            ans = ((x1-orix)**2 + (x2 - oriy)**2)

            return ans

        min_heap = []

        for i,point in enumerate(points):

            ans = calculate_dist(point[0],point[1])

            # heapq.heappush(min_heap, [-ans,i])
            heapq.heappush(min_heap, [-ans,point])

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        print(min_heap)


        # while k > 0:
        #     index = min_heap[0][1]
        #     heapq.heappop(min_heap)
        #     result.append(points[index])
        #     k-=1

        result = [point for _, point in min_heap]

        return result




        