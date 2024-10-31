class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        #brute
        # count = 0
        # n = len(time)
        
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if (time[i] + time[j]) % 60 == 0:
        #             count += 1
        
        # return count

        #optimzed
        remainder_count = defaultdict(int)
        count = 0

        for t in time:
            r = t % 60

            # Find the remainder that would make the sum a multiple of 60
            target = (60 - r) % 60

            # Add to count the number of times this target remainder has been seen
            if target in remainder_count:
                count += remainder_count[target]

            # Record the current remainder for future pairs
            remainder_count[r] += 1

        return count