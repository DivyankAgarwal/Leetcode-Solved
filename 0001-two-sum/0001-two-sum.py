class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #brute
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    

        # d = {}

        # for index, n in enumerate(nums):
        #     diff = target - n
        #     if diff in d:
        #         return [index,d[diff]]
        #     else:
        #         d[n] = index
        
        # return []


        
        