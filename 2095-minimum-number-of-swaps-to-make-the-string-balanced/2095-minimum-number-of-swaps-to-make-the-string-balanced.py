class Solution:
    def minSwaps(self, s: str) -> int:

        n = len(s)

        if len(s) % 2 != 0:
            return -1

        open = 0
        close = 0

        for bracket in range(n):
            if s[bracket] == '[':
                open +=1

            else:
                if open > 0:
                    open -= 1

                else:
                    close +=1

        print(open)
        print(close)

        ans = (close + 1) // 2

        return ans
        