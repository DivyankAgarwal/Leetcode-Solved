class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def find(index, sub, ans):
            
            if index < 0:
                ans.append(sub[:])
                return
            

            #pick
            sub.append(nums[index])
            find(index-1, sub, ans)
            sub.pop()

            #nonpick - skip duplicates
            while index > 0 and nums[index] == nums[index-1]:
                index-=1

            find(index-1, sub, ans)


        nums.sort()
        n = len(nums)
        ans = []
        find(n-1, [], ans)

        return ans
        