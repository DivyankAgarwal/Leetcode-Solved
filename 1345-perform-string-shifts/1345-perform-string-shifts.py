class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if len(s) == 0:
            return ''
        
        #brute
        for direction, amount in shift:
            amount = amount % len(s)
            if direction == 0:
                # Left shift
                s = s[amount:] + s[:amount]
            else:
                # Right shift
                s = s[-amount:] + s[:-amount]
        return s
        '''
        Time Complexity:
        Each shift operation takes O(n) time, where n is the length of the string, because slicing the string takes linear time.
        If there are k shift operations, the total time complexity is O(k * n).

        Space Complexity:
        We are creating new slices of the string after each shift, so the space complexity is O(n) to store the string.
        
        '''

        #optimized


        total_shift = 0
        n = len(s)
        
        # Calculate the net shift: left shifts subtract, right shifts add
        for direction, amount in shift:
            amount = amount % n
            if direction == 0:
                total_shift -= amount  
            else:
                total_shift += amount  

        # Get the effective shift (modulo length of string)
        total_shift = total_shift % n

        # Perform the final right shift
        if total_shift > 0:
            return s[-total_shift:] + s[:-total_shift]
        else:
            return s