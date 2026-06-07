class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Each land cell distance to nearest treasure chest
        #So bfs

        bfs = deque([])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                #There's a shit ton of repeated work
                #I find the treasure first
                #And bfs from there
                if grid[row][col] == 0:
                    #print("found")
                    bfs.append((row, col, 0))
        print(bfs)
        while bfs:
            #print(bfs)
            r, c, dist = bfs.popleft()
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]):
                continue
            if grid[r][c] < dist:
                continue
            else:
                grid[r][c] = dist
                #print(grid[r][c])
                bfs.append((r+1, c, dist+1))
                bfs.append((r-1, c, dist+1))
                bfs.append((r, c+1, dist+1))
                bfs.append((r, c-1, dist+1))
            #print(bfs)
