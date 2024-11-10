from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:


        def isValid(row,col):
            if row < 0 or row >= len(mat):
                return False

            if col < 0 or col >= len(mat[0]):
                return False

            return True

        distance = [ [0 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        visited = [ [0 for _ in range(len(mat[0]))] for _ in range(len(mat))]


        rows = len(mat)
        cols = len(mat[0])

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append([(r,c),0])
                    visited[r][c] = 1

        print(q)

        deltaRows = [-1,0,1,0]
        deltaCols = [0,1,0,-1]

        while q:

            for _ in range(len(q)):
                node, step = q.popleft()
                r = node[0]
                c = node[1]
                distance[r][c] = step

                for i in range(4):
                    nR = r + deltaRows[i]
                    nC = c + deltaCols[i]

                    if isValid(nR,nC) and visited[nR][nC] == 0:
                        visited[nR][nC] = 1
                        q.append([(nR, nC), step+1])
        
        return distance