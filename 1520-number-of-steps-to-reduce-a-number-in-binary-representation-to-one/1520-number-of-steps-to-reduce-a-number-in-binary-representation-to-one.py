class Solution:
    def numSteps(self, s: str) -> int:

        #brute

        # def addOne(s):
        #     #get intial pointer pointing to last

        #     pointer = len(s) - 1
        #     slist = list(s)

        #     while pointer >= 0 and slist[pointer] != "1":
        #         slist[pointer] = "0"
        #         pointer -=1

        #     if pointer == -1:
        #         slist = ["1"] + slist

        #     else:
        #         slist[pointer] = "1"

        #     return "".join(slist)


        # steps = 0
        # while s!= "1":
        #     #in binary, the last digit determines if no is even  or not

        #     if s[-1] == "0":
        #         s = s[:-1]

        #     else:
        #         s = addOne(s)

        #     steps +=1

        # return steps


        #optimal.
        
        
        # num = int(s, 2)  
        # steps = 0

       
        # while num != 1:
        #     if num % 2 == 0:  
        #         num //= 2     
        #     else:
        #         num += 1      
        #     steps += 1        

        # return steps


        #Optimal - without converting to integer

        steps = 0
        carry = 0  
        
        
        for i in reversed(range(1,len(s))):

            digit = (int(s[i]) + carry) % 2

            print(digit)

            if digit == 0:
                steps +=1
            
            elif digit == 1:
                steps += 2
                carry = 1

        return steps+carry