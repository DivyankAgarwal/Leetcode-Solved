class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        #brute

        # ans = 0

        # def get_largest_stone():

        #     stone1 = stones.index(max(stones))

        #     return stones.pop(stone1)

            
        
        # while len(stones) > 1:
        #     stone2 = get_largest_stone()
        #     stone1 = get_largest_stone()

        #     if stone1 != stone2:
        #         stones.append(-stone1 + stone2)

        # if stones:
        #     return stones[0]
        # else:
        #     return 0


        #Better

        min_heap = []

        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone2!= stone1:
                heapq.heappush(stones, stone1-stone2)

        if stones:
            return -heapq.heappop(stones)

        else:
            return 0



        