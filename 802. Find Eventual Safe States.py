

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        
        safe = set()
        visited = [0 for i in range(len(graph))]
        
        for i in range(len(graph)):
            if visited[i] == 0:
                self.dfs(graph,visited,i,safe)
        
        return sorted(safe)
    
    def dfs(self,graph,visited,i,safe):
        if visited[i] == 1:
            if i in safe:
                return True
            return False
        elif visited[i] == -1:
            return False
        
        visited[i] = -1
        isSafe = True
        for j in graph[i]:
            isSafe = self.dfs(graph,visited,j,safe) and isSafe
        
        visited[i] = 1
        if isSafe:
            safe.add(i)
        
        return isSafe