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