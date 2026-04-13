class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        if not grid:
            return 0
        
        queue = collections.deque()
        visit = set()
        islands = 0


        def bfs(r,c):
            queue.append((r,c))
            visit.add((r,c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if(0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"
                    and (nr,nc) not in visit):
                        queue.append((nr,nc))
                        visit.add((nr,nc))

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1  
    
        return islands


        