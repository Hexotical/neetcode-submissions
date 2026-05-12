class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        to_ret = []

        subset = []
        
        def dfs(i):
            if i >= len(nums):
                to_ret.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return to_ret

            