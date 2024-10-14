class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)

        cols = defaultdict(set)

        wholegrid = defaultdict(set)


        for r in range(9):
            for c in range(9):

                #1st. If it is empty, continue
                if board[r][c] == ".":
                    continue

                #2nd check if duplicate value present in hasheset

                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in wholegrid[(r//3,c//3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])

                wholegrid[(r//3,c//3)].add(board[r][c])

        return True
        