

#Topological Sort O(N+E)
#Need to optimize this solution
# Runtime: 182 ms, faster than 14.47% of Python online submissions

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g, inDegree = dict(), [0 for i in range(numCourses)]
        for i in range(numCourses):
            g[i] = []
        
        for dependency in prerequisites:
            inDegree[dependency[0]] += 1
            g[dependency[1]].append(dependency[0])
        
        if len(inDegree) == 0 :
            return True
        top = []
        
        stack = [ i for i in range(numCourses) if inDegree[i] == 0  ]
        
        while len(stack) > 0:
            i = stack[-1]
            del stack[-1]
            top.append(i)
            
            for j in g[i]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    stack.append(j)
        
        if len(top) != numCourses:
            return False
        return True
        

# Using DFS, O(V+E)
# Runtime: 125 ms, faster than 42.46% of Python online submissions 
class DFSSolution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for i in range(numCourses)]
        visited = [0 for i in range(numCourses)]
        
        for dependency in prerequisites:
            graph[dependency[1]].append(dependency[0])
        
        for i in range(numCourses):
            if self.isCyclicByDfs(i,graph,visited):
                return False
            
        return True
    
    def isCyclicByDfs(self,i,graph,visited):
        if visited[i] == -1: # sent to direct ancestor node, so cyclic
            return True
        
        if visited[i] == 1: # already visited and not direct ancestor 
            return False
        
        visited[i] = -1 # currently visiting this Node
        
        for j in graph[i]:
            if self.isCyclicByDfs(j,graph,visited):
                return True
        
        visited[i] = 1
        
        return False