class Solution:
    def reorganizeString(self, s: str) -> str:
        
        n = len(s)
        d = Counter(s)

        max_val = max(d.values())
        print(max_val)

        if max_val > (n+1) // 2:
            return ""

        sorted_chars = sorted(d.keys(), key=lambda x: -d[x])

        ans = [''] * len(s)

        print(sorted_chars)
        index = 0
        
        for char in sorted_chars:
            freq = d[char]

            for _ in range(freq):

                if index >= len(s):
                    index = 1

                ans[index] = char
                index+=2
        

        return ''.join(ans)



        
        