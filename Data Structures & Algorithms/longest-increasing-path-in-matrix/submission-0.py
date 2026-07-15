class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        long_start = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        #print(long_start)
        fun_heap = []
        heapq.heapify(fun_heap)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heapq.heappush(fun_heap, (-matrix[r][c], r, c))
        #print(fun_heap)
        longest_path = 0
        while fun_heap:
            val, row, col = heapq.heappop(fun_heap)
            if long_start[row][col] != -1:
                continue
            dfs = [(row, col, 1, matrix[row][col] + 1)]
            #print(dfs)
            while dfs:
                r, c, trail, val = dfs.pop()
                if r< 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
                    continue
                if long_start[r][c] >= trail:
                    continue
                if matrix[r][c] >= val:
                    continue
                long_start[r][c] = trail
                longest_path = max(longest_path, trail)
                dfs.append((r - 1, c, trail + 1, matrix[r][c]))
                dfs.append((r + 1, c, trail + 1, matrix[r][c]))
                dfs.append((r, c + 1, trail + 1, matrix[r][c]))
                dfs.append((r, c - 1, trail + 1, matrix[r][c]))
        #print(long_start)
        return longest_path
                
            
