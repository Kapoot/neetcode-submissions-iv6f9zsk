class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for src, dst in prerequisites:
            adjList[src].append(dst)

        visit = set()
        path = set()

        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True
            visit.add(i)
            path.add(i)

            for neighbor in adjList[i]:
                if not dfs(neighbor):
                    return False
            path.remove(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        
        