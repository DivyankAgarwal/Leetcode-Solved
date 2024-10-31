class Solution:
    def firstUniqChar(self, s: str) -> int:

        #brute
        # notfound = False
        # for i in range(len(s)):
        #     notfound = False
        #     for j in range(len(s)):
        #         if i != j and s[i] == s[j]:
        #             notfound = True
        #             break
        #         else:
        #             continue
        #     if not notfound:
        #         return i

        # return -1

        #optimzied
        d = collections.defaultdict(int)

        for i in s:
            d[i] +=1


        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

        return -1

        