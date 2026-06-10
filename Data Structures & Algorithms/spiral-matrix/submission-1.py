class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        to_ret = []
        dirs = [(0,1), (1,0), (0, -1), (-1,0)]
        min_row = 0
        max_row = len(matrix)
        min_col = -1
        max_col = len(matrix[0])
        cur_dir = 0
        cur_row = 0
        cur_col = 0
        while len(to_ret) < len(matrix) * len(matrix[0]):
            to_ret.append(matrix[cur_row][cur_col])
            if cur_dir == 0 and cur_col + dirs[cur_dir][1] == max_col:
                cur_dir = 1
                min_row = cur_row
            elif cur_dir == 1 and cur_row + dirs[cur_dir][0] == max_row:
                max_col = cur_col
                cur_dir = 2
            elif cur_dir == 2 and cur_col + dirs[cur_dir][1] == min_col:
                max_row = cur_row
                cur_dir = 3
            elif cur_dir == 3 and cur_row + dirs[cur_dir][0] == min_row:
                min_col = cur_col
                cur_dir = 0
            cur_row += dirs[cur_dir][0]
            cur_col += dirs[cur_dir][1]
           
        return to_ret