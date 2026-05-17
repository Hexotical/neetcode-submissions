class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Non duplicate subsets
        to_ret = []

        subset = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                to_ret.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        # to_ret = [set(x) for x in to_ret]
        # to_ret = set(to_ret)
        # to_ret = list(to_ret)
        return to_ret
