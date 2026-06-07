class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Bfs from the oceans?
        #Only if square is higher or equal than predecessor
        pacific_bfs = deque([])
        atlantic_bfs = deque([])
        pac_squares = set()
        atl_squares = set()
        for col in range(len(heights[0])):
            pacific_bfs.append((0, col, -1))
            atlantic_bfs.append((len(heights)-1, col, -1))
        
        for row in range(len(heights)):
            pacific_bfs.append((row, 0, -1))
            atlantic_bfs.append((row, len(heights[0])-1, -1))
        
        while pacific_bfs:
            row, col, prev_height = pacific_bfs.popleft()
            if row < 0 or col < 0 or row == len(heights) or col == len(heights[0]):
                continue
            if (row, col) in pac_squares:
                continue
            if heights[row][col] <prev_height:
                continue
            pac_squares.add((row,col))
            pacific_bfs.append((row-1, col, heights[row][col]))
            pacific_bfs.append((row+1, col, heights[row][col]))
            pacific_bfs.append((row, col-1, heights[row][col]))
            pacific_bfs.append((row, col+1, heights[row][col]))
        while atlantic_bfs:
            row, col, prev_height = atlantic_bfs.popleft()
            if row < 0 or col < 0 or row == len(heights) or col == len(heights[0]):
                continue
            if (row, col) in atl_squares:
                continue
            if heights[row][col] <prev_height:
                continue
            atl_squares.add((row,col))
            atlantic_bfs.append((row-1, col, heights[row][col]))
            atlantic_bfs.append((row+1, col, heights[row][col]))
            atlantic_bfs.append((row, col-1, heights[row][col]))
            atlantic_bfs.append((row, col+1, heights[row][col]))
        to_ret = atl_squares & pac_squares
        to_ret = list(to_ret)
        to_ret = [[a,b] for (a,b) in to_ret]
        return to_ret
        
