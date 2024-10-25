class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def isValid(row, col):

            if row<0 or row >= len(grid):
                return False

            if col<0 or col >= len(grid[0]):
                return False

            return True

        def dfs(row, col):

            grid[row][col] = '0'

            # directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            deltaRow = [-1,0,1,0]
            deltaCol = [0,1,0,-1]

            # for i in range(-1,2):
            #     for j in range(-1,2):
            # for dr, dc in directions:
            for i in range(4):

                newRow = row + deltaRow[i]
                newCol = col + deltaCol[i]

                if isValid(newRow, newCol) and grid[newRow][newCol] == '1':
                    dfs(newRow, newCol)


        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j)
        
        return count