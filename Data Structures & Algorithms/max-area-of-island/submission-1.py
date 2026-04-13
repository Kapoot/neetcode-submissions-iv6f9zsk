class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        
        queue = collections.deque()
        max_area = 0
        visited = set()

        def bfs(r,c):
            queue.append((r,c))
            visited.add((r,c))
            count = 1

            while queue:  
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if(0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1
                    and (nr,nc) not in visited):
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        count += 1
            
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    max_area = max(max_area, area)
        
        return max_area