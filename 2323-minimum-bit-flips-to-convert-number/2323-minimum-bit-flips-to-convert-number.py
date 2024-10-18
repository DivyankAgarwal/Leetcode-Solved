class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        # difference = start ^ goal

        # print(difference)
        # count  = 0

        # while difference:
        #     count+= difference & 1

        #     difference = difference >> 1

        # return count

        #optimal O(1)

        difference = start ^ goal

        count = 0

        for i in range(32):
            count += difference & 1

            difference  =  difference >> 1

        return count
        