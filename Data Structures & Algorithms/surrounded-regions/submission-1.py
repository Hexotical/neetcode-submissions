class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #I mean the way I want to do it is
        #Starting from any guaranteed unenclosed regions
        #bfs mark all connected parts
        #Then just go through and check for marked ones
        #Woo ok yea that's exactly what it wants from me
        bfs = deque([])
        free = set()
        for r in range(len(board)):
            if board[r][0] == "O":
                bfs.append((r, 0))
            if board[r][len(board[0])-1] == "O":
                bfs.append((r, len(board[0])-1))
        
        for c in range(len(board[0])):
            if board[0][c] == "O":
                bfs.append((0, c))
            if board[len(board)- 1][c] == "O":
                bfs.append((len(board)-1, c))
        
        while bfs:
            row, col = bfs.popleft()
            if (row, col) in free:
                continue
            if row < 0 or col < 0 or row == len(board) or col == len(board[0]):
                continue
            if board[row][col] == "X":
                continue
            free.add((row, col))
            bfs.append((row+1, col))
            bfs.append((row-1, col))
            bfs.append((row, col-1))
            bfs.append((row, col+1))

        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in free:
                    board[row][col] = "X"

