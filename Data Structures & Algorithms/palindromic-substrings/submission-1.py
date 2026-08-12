class Solution:
    def countSubstrings(self, s: str) -> int:
        #Dumbbbbb
        #I am dumb
        #Expand out
        to_ret =0
        #Odds
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                to_ret += 1
                l -= 1
                r += 1
        
        #Evens
        for i in range(1, len(s)):
            l = i -1
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                to_ret += 1
                l -= 1
                r += 1
        return to_ret

