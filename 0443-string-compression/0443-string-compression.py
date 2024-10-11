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

        write = 0
        count = 1
        
        for i in range(1, len(chars) + 1):
            
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            else:
                
                chars[write] = chars[i - 1]
                write += 1
                
                
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                
                
                count = 1
        
        return write
            