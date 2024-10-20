class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        diag_sum = 0
        n = len(mat)

        for i in range(len(mat)):
            #primary diagonal
            diag_sum += mat[i][i]

            #secondary diagonal
            diag_sum += mat[i][n-i-1]

        if n % 2 != 0:
            diag_sum -= mat[n//2][n//2]

        return diag_sum
        