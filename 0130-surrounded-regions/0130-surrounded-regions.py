class Solution:
    def solve(self, mat: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isValid(row, col):

            if row < 0 or row >= len(mat):
                return False

            
            if col < 0 or col >= len(mat[0]):
                return False

            return True



        def dfs(row, col,mat):
            
            mat[row][col] = "T"

            deltaRows = [-1,0,1,0]
            deltaCols = [0,1,0,-1]

            for i in range(4):
                nR = row + deltaRows[i]
                nC = col + deltaCols[i]

                if isValid(nR, nC) and mat[nR][nC] == "O":
                    dfs(nR, nC,mat)



        n = len(mat)
        m = len(mat[0])

        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if ( (i == 0 or i == n-1) or (j == 0 or j == m - 1)) and mat[i][j] == 'O':
                    dfs(i,j,mat)

        print(mat)

        
        #part 2

        for i in range(n):
            for j in range(m):
                if mat[i][j] == "O":
                    mat[i][j] = "X"



        #part 3

        for i in range(n):
            for j in range(m):
                if mat[i][j] == "T":
                    mat[i][j] = "O"
        