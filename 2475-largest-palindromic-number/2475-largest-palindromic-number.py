class Solution:
    def largestPalindromic(self, num: str) -> str:

        digit_counts = collections.Counter(num)

        front = []
        center = ''

        
        for digit in range(9,-1,-1):  
            digit_char = str(digit)

            if digit_char in digit_counts:
                count = digit_counts[digit_char]

                pairs = count // 2

                if pairs:
                    if not front and not digit:
                        digit_counts['0'] = 1
                    else:
                        front.append(digit_char * pairs)

                if count % 2 == 1 and not center:
                    center = digit_char
        
        if not center and not front:
            return "0"


        # Build the final palindrome
        front_part = ''.join(front)
        return front_part + center + front_part[::-1]