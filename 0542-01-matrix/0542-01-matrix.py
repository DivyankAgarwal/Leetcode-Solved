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

        print(distance)

        #bfs
        q = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if mat[i][j] == 0:
                    q.append([(i,j),0])
                    visited[i][j] = 1

        deltaRows = [-1,0,1,0]
        deltaCol = [0,1,0,-1]

        while q:

            for i in range(len(q)):

                data,step = q.popleft()
                row,col = data[0], data[1]
                
                distance[row][col] = step

                for i in range(4):
                    nR = row + deltaRows[i]
                    nC = col + deltaCol[i]

                    if isValid(nR, nC) and visited[nR][nC] == 0:

                        visited[nR][nC] = 1
                        q.append([(nR,nC), step+1])
        
        return distance



        