class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:


        def dfs(node, visited, graph, path, safestates):
            visited[node] = 1
            path[node] = 1

            for neighbour in graph[node]:

                if path[neighbour] == 1:
                    return True

                elif visited[neighbour] == 0:
                    if dfs(neighbour, visited, graph, path, safestates):
                        return True

            path[node] = 0
            safestates.append(node)
            return False

        visited = [0] * len(graph)
        path = [0] * len(graph)

        safestates = []

        for i in range(len(visited)):
            if visited[i] == 0:
                dfs(i, visited, graph, path, safestates)


        return sorted(safestates)
        

        