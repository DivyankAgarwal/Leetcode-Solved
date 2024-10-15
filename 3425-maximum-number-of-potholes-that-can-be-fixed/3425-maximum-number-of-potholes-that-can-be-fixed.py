class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:

        sequences = []
        n = len(road)
        i = 0

        
        while i < n:
            if road[i] == 'x':
                length = 0
                while i < n and road[i] == 'x':
                    length += 1
                    i += 1
                sequences.append(length)
            else:
                i += 1

        
        sequences.sort(reverse=True)

        total_potholes_fixed = 0
        remaining_budget = budget

        for length in sequences:
           
            cost = length + 1
            if cost <= remaining_budget:
                remaining_budget -= cost
                total_potholes_fixed += length
            else:
              
                max_potholes = min(length, remaining_budget - 1)
                if max_potholes >= 1:
                    cost = max_potholes + 1
                    if cost <= remaining_budget:
                        remaining_budget -= cost
                        total_potholes_fixed += max_potholes
              
                break

        return total_potholes_fixed

 