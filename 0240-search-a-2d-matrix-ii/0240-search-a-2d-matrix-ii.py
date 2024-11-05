class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        r = 0
        c = cols-1

        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True

            elif target > matrix[r][c]:
                r+=1

            else:
                c-=1

        return False
        