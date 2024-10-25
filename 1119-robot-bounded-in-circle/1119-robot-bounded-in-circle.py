class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y  = 0

        cur = 'N'

        for inst in instructions:
            if inst == 'G':
                if cur == 'N':
                    y +=1
                elif cur == 'W':
                    x -=1
                elif cur == 'S':
                    y -=1
                else:
                    x +=1
            
            else:
                if cur == 'N':
                    cur = 'W' if inst == 'L' else 'E'
                elif cur == 'W':
                    cur = 'S' if inst == 'L' else  'N'
                elif cur == 'S':
                    cur = 'E' if inst == 'L' else  'W'
                elif cur == 'E':
                    cur = 'N' if inst == 'L' else 'S'
        

        return (x == 0 and y == 0) or cur != 'N'

        