class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:


        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        def isValid(i,j):
            if i< 0 or i >= rows:
                return False


            if j < 0 or j >= cols:
                return False
            
            return True

        #brute

        # def find(i,j):
        #     if i == rows - 1 and j == cols - 1:
        #         return 1

        #     if not isValid(i,j) or obstacleGrid[i][j] == 1:
        #         return 0
            
        #     down = find(i+1,j)
        #     right = find(i,j+1)

        #     return down+right



        # rows = len(obstacleGrid)
        # cols = len(obstacleGrid[0])
        
        # return find(0,0)

        #memoization

        def find(i,j,dp):

            if i == rows - 1 and j == cols - 1:
                return 1

            if not isValid(i,j) or obstacleGrid[i][j] == 1:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            down = find(i+1,j,dp)
            right = find(i,j+1,dp)

            dp[i][j] = right+down
        
            return dp[i][j]

        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [ [-1 for _ in range(cols) ] for _ in range(rows)]

        return find(0,0, dp)
