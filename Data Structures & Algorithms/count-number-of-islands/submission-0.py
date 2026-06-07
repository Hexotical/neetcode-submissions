class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #so i think a dfs
        to_ret = 0
        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]):
                return
            if grid[row][col] == "0":
                return
            if (row, col) in visited:
                return
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) in visited:
                    continue
                if grid[row][col] == "0":
                    continue
                #print(row, col)
                to_ret += 1
                dfs(row, col)
        

        return to_ret