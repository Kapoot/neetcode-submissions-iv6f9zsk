class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        
        rows, cols = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        queue = collections.deque()
        minutes = 0
        oranges = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    oranges += 1
        
        while queue and oranges:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if(0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        oranges -= 1
            minutes += 1
        
        return minutes if oranges == 0 else -1