class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        
        graph = [[] for i in range(n)]
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
        
        ancestor = [set() for i in range(n)]
        predecessor = [set() for i in range(n)]
        
        visited = [0 for i in range(n)]
        
        for i in range(n):
            if visited[i] == 0:
                self.dfs(graph, i, visited, ancestor, predecessor)
        
        for i in range(len(ancestor)):
            ancestor[i] = sorted(ancestor[i])
        return ancestor
    
    def dfs(self,graph, i, visited, ancestor, predecessor):
        if visited[i] == 1:
            return predecessor[i]
        
        visited[i] = -1
        
        predecessor[i].add(i)
        
        for j in graph[i]:
            prJ = self.dfs(graph, j, visited, ancestor, predecessor)
            
            for k in prJ:
                ancestor[k].add(i)
            
            predecessor[i].update(prJ)
        
        visited[i] = 1
        
        return predecessor[i]
        
