class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        #brute

        ans = 0

        def get_largest_stone():

            stone1 = stones.index(max(stones))

            return stones.pop(stone1)

            
        
        while len(stones) > 1:
            stone2 = get_largest_stone()
            stone1 = get_largest_stone()

            if stone1 != stone2:
                stones.append(-stone1 + stone2)

        if stones:
            return stones[0]
        else:
            return 0



        