class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node, adjList, visited):
            visited[node] = 1

            for neighbour in adjList[node]:
                if visited[neighbour] == 0:
                    dfs(neighbour, adjList, visited)

        #convert matrix to adjList

        adjList = [[] for _  in range(len(isConnected))]

        V = len(isConnected)

        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i!=j:
                    adjList[i].append(j)
                    adjList[j].append(i)

        count = 0
        visited = [0] * V

        for i in range(V):
            if visited[i] == 0:
                count+=1
                dfs(i, adjList, visited)

        return count
        