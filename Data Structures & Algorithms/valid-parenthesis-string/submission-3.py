class Solution:
    def checkValidString(self, s: str) -> bool:
        #Stackkkk
        braces = []
        stars = []
        for i, c in enumerate(s):
            if c == "(":
                braces.append(i)
            elif c == "*":
                stars.append(i)
            else:
                if len(braces) > 0:
                    braces.pop()
                elif len(stars) > 0:
                    stars.pop(0)
                else:
                    return False
        while braces:
            check = braces.pop()
            if not stars or check > stars[-1]:
                return False
            stars.pop()
        return True


        #Order matters which is why this doesnt work, not every 
        #star can offset open left brackets
        return braces == 0 or braces <= stars