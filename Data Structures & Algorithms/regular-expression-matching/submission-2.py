class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #True if pattern matches entire string
        #False if otherwise
        #. is any character
        #* matches zero or more of preceeding element
        memo = dict()
        def helper(si, pi):
            if (si, pi) in memo:
                return memo[(si, pi)]
            print(si, pi)
        
            if si == len(s) and pi == len(p):
                memo[(si, pi)] = True
                return True
            if pi == len(p) and si < len(s):
                memo[(si, pi)] = False
                return False
            if si == len(s):
                while pi < len(p):
                    if pi < len(p) - 1:
                        if p[pi + 1] == "*":
                            pi += 2
                        else:
                            return False
                    else:
                        return False
                return True
            if p[pi] == ".":
                if si >= len(s):
                    memo[(si, pi)] = False
                    return False
                if pi < len(p) - 1:
                    if p[pi+1] == "*":
                        return helper(si, pi + 1)
                return helper(si + 1, pi + 1)
            elif p[pi] == "*":
                pos = helper(si, pi + 1) #base case of 0

                for j in range(si, len(s)): 
                    if p[pi-1] == '.' or p[pi-1] == s[j]:
                        pos |= helper(j + 1, pi + 1)
                    else:
                        break
                memo[(si, pi)] = pos
                return pos
            else:
                if si >= len(s):
                    memo[(si, pi)] = False
                    return False
                if p[pi] == s[si]:
                    if pi < len(p) - 1:
                        if p[pi + 1] == "*":
                            memo[(si, pi)] = helper(si, pi + 1)
                        else: 
                            memo[(si, pi)] = helper(si + 1, pi + 1)
                    else:
                        memo[(si, pi)] = helper(si + 1, pi + 1)
                    return memo[(si, pi)]
                else:
                    if pi < len(p) - 1:
                        if p[pi + 1] == "*":
                            memo[(si, pi)] = helper(si, pi + 1)
                        else: memo[(si, pi)] = False
                    else:
                        memo[(si, pi)] = False
                    return memo[(si, pi)]
        return helper(0, 0)