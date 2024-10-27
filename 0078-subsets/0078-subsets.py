class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def generateseq(index, sub):
            if index >= n:
                result.append(sub[:])
                return

            generateseq(index+1, sub) #print empty
            sub.append(nums[index])
            generateseq(index+1, sub)
            sub.remove(nums[index])
            

        result = []
        n = len(nums)
        generateseq(0, [])

        return result
        