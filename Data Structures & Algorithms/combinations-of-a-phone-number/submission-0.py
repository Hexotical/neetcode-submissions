class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #All possible letter combinations digits could represent
        word_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        if not digits:
            return []
        to_ret = []
        running_str = []

        def dfs(i):
            if i >= len(digits):
                to_ret.append("".join(running_str))
                return
            for c in word_map[digits[i]]:
                running_str.append(c)
                dfs(i + 1)
                running_str.pop()
        
        dfs(0)
        return to_ret