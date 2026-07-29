class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #All combinations of k numbers in range up to n
        to_ret = []
        cur_group = []

        def recur(i):
            if len(cur_group) == k:
                to_ret.append(cur_group.copy())
                return
            if i > n:
                return
            cur_group.append(i)
            recur(i+1)
            cur_group.pop()
            recur(i+1)
            
        recur(1)
        return to_ret