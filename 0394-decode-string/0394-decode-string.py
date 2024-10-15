class Solution:
    def decodeString(self, s: str) -> str:

        #brute
        stack = []
        currentNo = 0
        currentString = ''
    

        for char in s:
            #check if no
            if char.isdigit():
                currentNo = currentNo * 10 + int(char)

            elif char == '[':
                stack.append([currentString, currentNo])
                currentNo = 0
                currentString = ''

            elif char == ']':
                last_string, count = stack.pop()
                currentString  =  last_string + count * currentString

            else:
                currentString += char

        
        return currentString
        