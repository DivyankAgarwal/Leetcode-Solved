class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        

        for spell in spells:
            left = 0
            right = len(potions) - 1
            index = len(potions)

            while left <= right:
                mid = left + (right - left) // 2

                if potions[mid] * spell >= success:
                    right = mid - 1
                    index = mid

                else:
                    left = mid +1
            
            result.append(len(potions) - index)
    
        return result
            