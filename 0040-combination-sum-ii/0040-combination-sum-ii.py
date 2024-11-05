class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def find(index, dummy, sub, ans, target):
            if target == 0:
                ans.append(sub[:])
                return

            if index == len(dummy) or target < 0:
                return
            

            # #exclude
            # find(index-1,dummy, sub, ans, target)

            sub.append(dummy[index])

            find(index+1, dummy,sub, ans,target-dummy[index])

            sub.pop()

            #special exclude logic. dont consider duplicate values.
            for i in range(index + 1, len(dummy)):
                if dummy[i] != dummy[index]:
                    find(i, dummy, sub,ans,target)
                    break




        candidates.sort()
        dummy = candidates[:]
        ans = []
        

        n = len(candidates)

        find(0, dummy,[], ans, target)

        return ans