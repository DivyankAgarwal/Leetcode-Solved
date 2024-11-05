class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def find(index, dummy, ans, sub, target):

            if target == 0:
                ans.append(sub[:])
                return

            if index < 0 or target < 0:
                return 
            

            #exclude
            find(index-1, dummy, ans, sub, target)

            sub.append(dummy[index])

            find(index, dummy,ans, sub, target - dummy[index])

            sub.pop()



        ans = []

        n = len(candidates)
        dummy = candidates[:]

        find(n-1, dummy,ans, [],target)

        return ans
        