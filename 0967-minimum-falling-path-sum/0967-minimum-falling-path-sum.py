class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #brute - recursive TC: O(3^n)
    #     n = len(matrix)

    #     def minPath(i, j):
    #         # Base case: If we're at the last row, return the value of the current cell
    #         if i == n - 1:
    #             return matrix[i][j]

    #         # Initialize a large number for comparison
    #         down = minPath(i + 1, j) if i + 1 < n else float('inf')
    #         left = minPath(i + 1, j - 1) if i + 1 < n and j - 1 >= 0 else float('inf')
    #         right = minPath(i + 1, j + 1) if i + 1 < n and j + 1 < n else float('inf')

    #         # Recursive relation to find the minimum path sum for the current cell
    #         return matrix[i][j] + min(down, left, right)

    # # Start the recursion from each cell in the first row and find the minimum path sum
    #     return min(minPath(0, j) for j in range(n))

    #memoization TC:O(n2)

        # def minPath(r,c):
        #     if r == rows - 1:
        #         return matrix[r][c]

        #     if dp[r][c] != -1:
        #         return dp[r][c]

        #     down = minPath(r+1,c) if r+1 < rows else float('inf')
        #     left = minPath(r+1,c-1) if r+1 < rows and c-1 >=0 else float('inf')
        #     right = minPath(r+1,c+1) if r+1 < rows and c+1 < cols else float('inf')

        #     dp[r][c] = matrix[r][c] +  min(down,left,right)
        #     return dp[r][c]


        # rows = len(matrix)
        # cols = len(matrix[0])

        # dp = [[-1 for _ in range(cols)] for _ in range(rows)]
        # return min(minPath(0, j) for j in range(rows))

        #tabulation - bottom up

        n = len(matrix)
        
        dp = matrix[-1][:]  # Copy of the last row as base case
        
        for i in range(n - 2, -1, -1):
            # Temporary storage for the current row to avoid overwriting
            new_dp = [0] * n
            for j in range(n):
                # Calculate minimum path sum for each cell in the current row
                down = dp[j]
                left = dp[j - 1] if j > 0 else float('inf')
                right = dp[j + 1] if j < n - 1 else float('inf')

                # Update the current cell's minimum path sum
                new_dp[j] = matrix[i][j] + min(down, left, right)

            # Move to the next row up by updating dp to the newly calculated row
            dp = new_dp

        return min(dp)

        
