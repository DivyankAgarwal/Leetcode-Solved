class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        #brute TC: O(n + m); SC: O(n + m)
        # s1 = []
        # s2 = []

        # for char in s:
        #     if char == '#':
        #         if s1:
        #             s1.pop()

        #     else:
        #         s1.append(char)

        # for char in t:
        #     if char == '#':
        #         if s2:
        #             s2.pop()

        #     else:
        #         s2.append(char)
        
        # return s1 == s2

        #space optimized.
        i, j = len(s) - 1, len(t) - 1
        
        def getValidIndex(string, index):
            backspace = 0
            while index >= 0:
                if string[index] == '#':
                    backspace += 1
                elif backspace > 0:
                    backspace -= 1
                else:
                    return index
                index -= 1
            return -1

        while i >= 0 or j >= 0:
            i = getValidIndex(s, i)
            j = getValidIndex(t, j)
            
            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0 or s[i] != t[j]:
                return False
            
            i -= 1
            j -= 1
            
        return True