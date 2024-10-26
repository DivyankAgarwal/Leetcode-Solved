class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #brute TC: O(2^(m+n)), where m and n are the grid dimensions. 
        #This is because each cell has two choices (down or right), resulting in an exponential number of recursive calls.


        # def isValid(i,j):
        #     if i < 0 or i >= len(grid):
        #         return False

        #     if j < 0 or j>= len(grid[0]):
        #         return False

        #     return True

        # def dfs(i, j):
        
        # #reached the end
        #     if i == len(grid) - 1 and j == len(grid[0]) - 1:
        #         return grid[i][j]
            
        
        #     if not isValid(i,j):
        #         return float('inf')
            
        
        #     return grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))
        
        # return dfs(0, 0)


        #Optimized

        m, n = len(grid), len(grid[0])
    
        # Fill the first row
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        
        # Fill the first column
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        
        # Fill in the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]  