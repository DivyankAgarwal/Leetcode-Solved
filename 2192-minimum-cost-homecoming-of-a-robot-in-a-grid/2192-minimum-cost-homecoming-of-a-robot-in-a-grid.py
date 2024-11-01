class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        cost = 0
        startx, starty = startPos
        endx, endy = homePos
        path = []


        #calculating cost for row
        while startx != endx:
            if startx < endx:
                startx +=1
            else:
                startx -=1
            
            cost += rowCosts[startx]
            path.append((startx,starty))



        #calclating cost for col

        while starty != endy:
            if starty < endy:
                starty +=1
            else:
                starty -=1
            
            cost += colCosts[starty]
            path.append((startx,starty))


        print(path)
        return cost