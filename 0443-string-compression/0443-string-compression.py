class Solution:
    def compress(self, chars: List[str]) -> int:
        # result = []

        # count = 1

        # for i in range(1, len(chars)):

        #     if chars[i] == chars[i-1]:
        #         count +=1

        #     else:
        #         if count == 1:
        #             result.append(chars[i-1])
        #         else:
        #             result.append(chars[i-1])
        #             result.append(str(count))
        #             count = 1

        # if count == 1:
        #     result.append(chars[-1])
        # else:
        #     result.append(chars[-1])
        #     result.append(str(count))

        # return len(result)

        read, write = 0, 0
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            
            while read < n and chars[read] == char:
                count += 1
                read += 1
            
            
            chars[write] = char
            write += 1
            
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write 