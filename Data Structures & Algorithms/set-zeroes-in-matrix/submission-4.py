class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #Constant space??
        #mn2 approach for it
        #I mean constant space given the hints
        #Binary representation of the rows/cols and then going through
        #If the row or col is 0 i give that square a 0
        #2 passes one for marking rows/ columns
        #one fo

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    if matrix[r][0] != "rc":
                        matrix[r][0] = "r"
                    if c == 0 and matrix[0][0] == "r":
                         matrix[r][c] = "rc"
                    else:
                        if c == 0 and matrix[0][0] == "rc":
                            continue
                        matrix[0][c] = "c"
                    
        print(matrix)
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == "c":
                for r in range(len(matrix)):
                    matrix[r][c] = 0
        for r in range(1, len(matrix)):
            if matrix[r][0] == "r":
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0
        if matrix[0][0] == "c":
            for r in range(len(matrix)):
                matrix[r][0] = 0
        if matrix[0][0] == "r":
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if matrix[0][0] == "rc":
            for r in range(len(matrix)):
                matrix[r][0] = 0
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
                
                