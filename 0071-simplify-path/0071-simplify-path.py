class Solution:
    def simplifyPath(self, path: str) -> str:

        result = ''

        stack = []

        inp = path.split('/')

        print("intput", inp)

        for s in inp:
            if s == '..':
                if stack:
                    stack.pop()
            
            elif s == '.' or s == "" :
                continue

            else:

                stack.append(s)

        print("Stack: ",stack)

        result = "/"

        if len(stack) != 0:

            for i in range(len(stack)):
                result += stack[i] + "/"

            n = len(result)

            return result[:n-1]
        else:
            return result

        

        