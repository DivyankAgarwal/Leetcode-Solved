class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        #brute
        # result = []
       
        # count = {'a': a, 'b': b, 'c': c}
        
        # while True:
           
        #     chars = sorted(count, key=lambda x: -count[x])  # Sort by count, descending
            
        #     # Find the most frequent character to add
        #     added = False
        #     for char in chars:
               
        #         if len(result) >= 2 and result[-1] == char and result[-2] == char:
        #             continue  

        #         if count[char] > 0:
        #             result.append(char)
        #             count[char] -= 1
        #             added = True
        #             break  
            
        #     if not added:
        #         break 

        # return ''.join(result)
        
        #optimal - heap

        temp = [[a,'a'],[b,'b'],[c,'c']]
        result = ''
        maxheap = []

        for count, char in temp:
            if count != 0:
                heapq.heappush(maxheap, [-count,char])

       
        print(maxheap)

        while maxheap:
            count, char = heapq.heappop(maxheap)

            if len(result) > 1 and result[-1] == result[-2] == char:
                if not maxheap:
                    break
                else:
                    count2, char2 = heapq.heappop(maxheap)



                    result += char2
                    count2 +=1

                    if count2:
                        heapq.heappush(maxheap, [count2, char2])

            else:
                result += char
                count +=1

            if count:
                heapq.heappush(maxheap, [count, char])

        return result




