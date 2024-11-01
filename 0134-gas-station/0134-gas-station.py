class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        startIndex = 0
        gasCount = 0
        i = 0

        while i < len(gas):
            gasCount  += gas[i] - cost[i]

            if gasCount < 0:
                startIndex = i +1
                gasCount = 0
            i+=1

        return startIndex