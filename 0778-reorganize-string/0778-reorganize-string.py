class Solution:
    def reorganizeString(self, s: str) -> str:
        
        # n = len(s)
        # d = Counter(s)

        # max_val = max(d.values())
        # print(max_val)

        # if max_val > (n+1) // 2:
        #     return ""

        # sorted_chars = sorted(d.keys(), key=lambda x: -d[x])

        # ans = [''] * len(s)

        # print(sorted_chars)
        # index = 0
        
        # for char in sorted_chars:
        #     freq = d[char]

        #     for _ in range(freq):

        #         if index >= len(s):
        #             index = 1

        #         ans[index] = char
        #         index+=2
        

        # return ''.join(ans)


        #using max heap

        n = len(s)
        d = Counter(s)

        max_val = max(d.values())
        print(max_val)

        if max_val > (n+1) // 2:
            return ""
        
        max_heap = [(-freq, char) for char, freq in d.items()]
        heapq.heapify(max_heap)
        ans = []
        prev_char = ''
        prev_count = 0
        while max_heap:

            count,char = heapq.heappop(max_heap)

            ans.append(char)
            
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

            # Update previous character and frequency (decrease current character's frequency)
            prev_char, prev_count = char, count + 1

        
        return ''.join(ans)






        
        