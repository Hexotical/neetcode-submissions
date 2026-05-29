class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #No repeated squares

       
        visited = set()
        def backtrack(row, col, i):
            if i == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            if (row, col) in visited:
                return False
            if board[row][col] != word[i]:
                return False
            visited.add((row, col))
            res = (backtrack(row +1, col, i + 1) or
                    backtrack(row -1, col, i + 1) or
                    backtrack(row, col + 1, i + 1) or
                    backtrack(row , col-1, i + 1) )
            
            visited.remove((row, col))
            return res

            
            

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True

        return False