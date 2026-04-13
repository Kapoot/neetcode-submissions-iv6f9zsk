class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        queue = collections.deque()
        fresh_fruit = 0
        rows, cols = len(grid), len(grid[0])
        minute = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh_fruit += 1
        
        if fresh_fruit == 0:
            return 0
        
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        
        while queue and fresh_fruit > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if(nr >= 0 and nr < rows and nc >= 0 and nc < cols and
                    grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh_fruit -= 1
                        queue.append((nr,nc))
            
            minute += 1
        
        return minute if fresh_fruit == 0 else -1
            

        