class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        to_ret = []
        cur_group = []

        def recur(num):
            
            if len(cur_group) == k:
                to_add = cur_group.copy()
                to_ret.append(to_add)
                return
            if num > n:
                return
            cur_group.append(num)
            recur(num+1)
            cur_group.pop()
            recur(num+1)
        recur(1)
        return to_ret