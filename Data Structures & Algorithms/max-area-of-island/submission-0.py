class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Biggest island we find 
        #Dfs basically same as num islands
        #but keep track of how many cells we visit each time

        visited = set()

        def dfs(row, col):
            if row <0 or col <0 or row == len(grid) or col == len(grid[0]):
                return
            if (row, col) in visited:
                return
            if grid[row][col] == 0:
                return
            visited.add((row, col))
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        to_ret = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    prev = len(visited)
                    #print(prev)
                    dfs(row, col)
                    #print(len(visited))
                    to_ret = max(to_ret, len(visited) - prev)
        

        return to_ret