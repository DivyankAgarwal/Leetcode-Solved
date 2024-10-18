class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #brute
        # d = defaultdict(int)

        # for n in nums:
        #     d[n] +=1

        # for k,v in d.items():
        #     if v == 1:
        #         return k
        
        # return -1


        #Space O(1)

        result = 0

        for n in nums:
            result = result ^ n

        return result

        
        