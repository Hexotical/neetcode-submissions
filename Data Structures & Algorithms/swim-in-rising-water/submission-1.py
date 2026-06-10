class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Starting from top left
        #min time to reach bottom right square
        #At every step water level increases, 
        #Can swim to adjacent square if both elevations are less than or equal to the water
        min_time = float('inf')
        bfs = []
        heapq.heapify(bfs)
        heapq.heappush(bfs, (grid[0][0], 0, 0))

        memo = dict()
        #Ohh time is just when possible to swim to the bottom

        while bfs:
            time, row, col = heapq.heappop(bfs)
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                continue
            time = max(grid[row][col], time)
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                #print("we found this?")
                return time
            
            if (row, col) in memo and memo[(row, col)] <= time:
                #I've reached this square and processed the neighbors
                memo[(row, col)] = time
                continue
            memo[(row, col)] = time
            heapq.heappush(bfs, (time, row+1, col))
            heapq.heappush(bfs, (time, row-1, col))
            heapq.heappush(bfs, (time, row, col-1))
            heapq.heappush(bfs, (time, row, col+1))
        #print(memo[(len(grid)-1, len(grid[0])-1)])
        return grid[len(grid)-1][len(grid[0])-1]






