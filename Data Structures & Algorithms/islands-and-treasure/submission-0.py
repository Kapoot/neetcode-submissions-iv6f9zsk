class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        queue = collections.deque()
       
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if(0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF):
                    queue.append((nr,nc))
                    grid[nr][nc] = grid[row][col] + 1
