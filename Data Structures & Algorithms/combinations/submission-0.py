class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #numbers

        to_ret = []
        cur_group = []
        def recur(i):
            if len(cur_group) == k:
                to_ret.append(cur_group.copy())
                return
            if i > n:
                return
            #otherwise we can either add the number to cur_group
            cur_group.append(i)
            recur(i+1)
            cur_group.pop()
            recur(i+1)
            
            #Options are either
            #Include the number
            #not include number

        recur(1)

        return to_ret