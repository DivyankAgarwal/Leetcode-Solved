class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def isValid(r,c):
            if r < 0 or r >= rows:
                return False

            if c < 0 or c >= cols:
                return False
            

            return True

        def dfs(r,c,word,k):
            if k == len(word):
                return True


            if not isValid(r,c) or word[k] != board[r][c]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
           

            deltaRow = [-1,0,1,0]
            deltaCol = [0,1,0,-1]

            for i in range(4):
                nR = r + deltaRow[i]
                nC = c + deltaCol[i]

                if dfs(nR,nC, word, k+1):
                     return True
            
            board[r][c] = temp
            return False


        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r,c,word,0):
                    return True

        return False
        