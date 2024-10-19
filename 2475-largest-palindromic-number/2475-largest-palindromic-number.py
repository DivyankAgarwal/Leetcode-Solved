from itertools import permutations

class Solution:
    def largestPalindromic(self, num: str) -> str:

        #brute

        '''
        The brute force method could involve generating all possible permutations of the 
        digits, checking for palindromes, and then selecting the 
        largest one. However, this approach would be highly inefficient 
        due to the factorial growth of permutations, especially with longer input strings.

      
        perms = set(permutations(num))
        max_palindrome = ''
        for perm in perms:
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                if candidate > max_palindrome:
                    max_palindrome = candidate
        return max_palindrome if max_palindrome else '0'

        '''
        #optimal
        digit_counts = collections.Counter(num)

        front = []
        center = ''

        
        for digit in reversed(range(0,10)):  
            digit_char = str(digit)


            if digit_char in digit_counts:
                count = digit_counts[digit_char]


                pairs = count // 2

                if pairs != 0:
                    if len(front) == 0 and digit == 0:
                        
                        # digit_counts['0'] = 1
                        continue
                    else:
                        front.append(digit_char * pairs)

                if count % 2 == 1 and not center:
                    center = digit_char
        

    
        front_part = ''.join(front)
        palindrome = front_part + center + front_part[::-1]

        if palindrome.lstrip('0') == '':  
            return '0'
        else:
            return palindrome