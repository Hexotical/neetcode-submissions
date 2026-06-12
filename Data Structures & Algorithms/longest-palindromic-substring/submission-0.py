class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Longest substring of s that is a palindrome
        #so n^2 would be for each character
        #try building a palindrome centered there
        #Oh i mean this is just the solution lol
        #I thought they'd do something more clever
        to_ret = 0
        substr = ""
        for i, v in enumerate(s):
            attempt = 0
            l = r = i
            while l > -1 and r < len(s) and s[l] == s[r]:
                attempt = r-l + 1
                if attempt > len(substr):
                    substr = s[l:r+1]
                
                l -= 1
                r += 1
            #Need to deal with even centers
            if i > 0 and s[i] == s[i-1]:
                l = i-1
                r = i
            while l > -1 and r < len(s) and s[l] == s[r]:
                attempt = r-l + 1
                if attempt > len(substr):
                    substr = s[l:r+1]
                l -= 1
                r += 1
            
        
        return substr