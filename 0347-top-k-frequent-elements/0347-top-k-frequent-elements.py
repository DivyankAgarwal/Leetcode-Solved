class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = Counter(nums)

        d = sorted(d.items(), key = lambda x : (-x[1]))
        ans = []

        for a,v in d:
            if k != 0:
                ans.append(a)
                k-=1
            
            if k == 0:
                break
        
        return ans
        