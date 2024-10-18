class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        #brute
        d = collections.defaultdict(int)
        result = []

        for n in nums:
            d[n] +=1


        for k, v in d.items():
            if v == 1:
                result.append(k)
        return result
        