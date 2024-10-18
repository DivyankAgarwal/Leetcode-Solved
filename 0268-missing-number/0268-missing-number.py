class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # n = len(nums)

        # s1 = sum(nums)

        # s2 = ( n * (n+1) ) // 2

        # return s2 -s1
        


        #using Bitwise


        xor1 = 0
        xor2 = 0

        for n in nums:
            xor1 = xor1 ^ n

        for i in range(len(nums)+1):
            xor2 = xor2 ^ i

        return xor2 ^ xor1