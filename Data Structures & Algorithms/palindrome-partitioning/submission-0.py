class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #Substringsss
        #Continous portion
        #Windows of varrying sizes?
        #I mean i wanna just do different sized windows
        #Ahhhh
        #all possible lists of palindromic substrings
        def isPalindrome(s):
            if s == s[::-1]:
                return True
            else:
                return False
        to_ret = []

        cur_part_list = []
        def backtrack(j, i):

            if i >= len(s):
                if j == len(s):
                    to_ret.append(cur_part_list.copy())
                return
            

            if isPalindrome(s[j:i+1]):
                cur_part_list.append(s[j:i+1])
                backtrack(i+1, i+1)
                cur_part_list.pop()
            
            if i + 1 < len(s):
                backtrack(j, i+1)

        backtrack(0,0)
        return to_ret