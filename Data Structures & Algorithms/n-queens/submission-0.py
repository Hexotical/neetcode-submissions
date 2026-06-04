class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)] 
        #List all distinct solutions
        def check_col(col):
            #Return True if queen already in column
            for row in range(n):
                if board[row][col] == "Q":
                    return False
            return True

        def check_row(row):
            for col in range(n):
                if board[row][col] == "Q":
                    return False
            return True

        def check_diag(row, col):
            #Up and to the left
            for i in range(row + 1):
                #Cover the left
                if col - i >= 0 and board[row-i][col-i] == "Q":
                    return False
                if col + i < n and board[row-i][col+i] == "Q":
                    return False
            for i in range(n - row):
                if col - i >= 0 and board[row+i][col-i] == "Q":
                    return False
                if col + i < n and board[row+i][col+i] == "Q":
                    return False
            return True



            #Up and to the right
            #Down to the left
            #down to the right
        to_ret = []
        def backtrack(row, placed):
            #print(row, placed)
            if row >= n and placed == n:
                #print(row, placed)
                copy = []
                for row in board:
                    copy.append("".join(row))
                to_ret.append(copy)
                return
            #Otherwise we try and place a queen 
            for col in range(n):
                if not check_col(col):
                     continue
                if not check_diag(row, col):
                    continue
                board[row][col] = "Q"
                backtrack(row+1, placed+1)
                board[row][col] = "."


        backtrack(0, 0)
        return to_ret
