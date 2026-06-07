class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Bfs 
        rotten = dict()
        bfs = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    bfs.append((r, c, 0))
                    rotten[(r,c)] = 0
        #Track all fresh fruit
        #Ok that's literally what it says that's annoying
        
        while bfs:
            row, col, time = bfs.popleft()
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]):
                continue
            if grid[row][col] == 0:
                continue
            if (row, col) in rotten and rotten[(row,col)] < time:
                continue
            rotten[(row,col)] = time
            bfs.append((row+1, col, time+1))
            bfs.append((row-1, col, time+1))
            bfs.append((row, col-1, time+1))
            bfs.append((row, col+1, time+1))
        to_ret = 0
        #print(rotten)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    if (r, c) not in rotten:
                        return -1
                    else:
                        to_ret = max(to_ret, rotten[(r,c)])
        return to_ret