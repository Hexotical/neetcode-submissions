class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Rotate in place
        
        matrix.reverse()
        #So i just swap
        #row, col -> col, n-row
        
        for row in range(len(matrix)):
            for col in range( row + 1, len(matrix[0])):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = tmp