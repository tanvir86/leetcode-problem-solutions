

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
        