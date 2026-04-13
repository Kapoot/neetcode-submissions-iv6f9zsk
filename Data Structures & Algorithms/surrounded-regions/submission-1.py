class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return None
        
        rows, cols = len(board), len(board[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        queue = deque()
        visited = set()

        def add(r, c):
            if (r, c) not in visited and board[r][c] == "O":
                queue.append((r, c))
                visited.add((r, c))

        # top and bottom rows
        for c in range(cols):
            add(0, c)
            add(rows - 1, c)

        # left and right columns
        for r in range(rows):
            add(r, 0)
            add(r, cols - 1)

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if(0 <= nr < rows and 0 <= nc < cols and
                board[nr][nc] == "O" and (nr,nc) not in visited):
                    queue.append((nr,nc))
                    visited.add((nr,nc))
        

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"
        
                    