class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        #brute

        # i = 0
        # ans = 0

        # if len(g) == 0 or len(s) == 0:
        #     return 0

        # while i < len(g):
        #     max1 = max(g)
        #     max2 = max(s)

        #     if max1 <= max2:
        #         ans +=1
        #         idx1 = g.index(max1)
        #         idx2 = s.index(max2)

        #         g[idx1] = -1
        #         s[idx2] = -1
        #         i+=1
        #     else:
        #         idx1 = g.index(max1)
        #         g[idx1] = -1
        #         i+=1

        # return ans

        i = 0
        j = 0

        g.sort()
        s.sort()

        ans = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ans +=1
                i+=1
                j+=1
            else:
                j+=1
        return ans

        