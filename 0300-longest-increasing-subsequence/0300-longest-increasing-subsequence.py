class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #brute
        def find(index, prev):

            if index == n:
                return 0
            
            nonpick = find(index+1, prev)

            pick = 0
            if prev == -1 or nums[index] > nums[prev]:
                pick = 1 + find(index+1, index)


            return max(pick, nonpick)


        n = len(nums)
        return find(0,-1)
        