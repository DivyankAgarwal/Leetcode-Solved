class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def isValid(r,c):
            if r < 0 or r >= len(grid):
                return False

            if c < 0 or c >= len(grid[0]):
                return False

            return True


        def dfs(row,col,visited):
            if  not isValid(row, col) or grid[row][col] == 0 or (row, col) in visited:
                return 0

            visited.add((row,col))
            current_gold = grid[row][col]
            max_gold = 0

            deltaRow = [-1,0,1,0]
            deltaCol = [0,1,0,-1]

            for i in range(4):
                nR = row + deltaRow[i]
                nC = col + deltaCol[i]

                max_gold = max(max_gold, dfs(nR, nC, visited))

            visited.remove((row,col))
            
            return current_gold + max_gold


        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 0:
                    result = max(result, dfs(row, col, set()))

        return result
        