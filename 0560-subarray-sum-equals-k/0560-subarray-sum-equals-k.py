class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #Brute
        # count = 0
        # for start in range(len(nums)):
        #     sum = 0
        #     for end in range(start, len(nums)):
        #         sum += nums[end]
                
        #         if sum == k:
        #             count +=1
        # return count

        #optimal

        result = 0
        currentSum = 0

        prefixmap = {0: 1} 

        for n in nums:
            currentSum += n

            if currentSum - k in prefixmap:
                result += prefixmap[currentSum - k]

            if currentSum in prefixmap:
                prefixmap[currentSum] +=1
            else:
                prefixmap[currentSum] = 1

        return result
