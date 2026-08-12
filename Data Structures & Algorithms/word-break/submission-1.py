class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = dict()
        for w in wordDict:
            memo[w] = True
        def helper(test):
            if test in memo:
                return memo[test]
            #Test for prefixes 
            check = False
            for pre in wordDict:
                if test.startswith(pre):
                    check |= helper(test[len(pre):])
            memo[test] = check
            return memo[test]
        
        return helper(s)

