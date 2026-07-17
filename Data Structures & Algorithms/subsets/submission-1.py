class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        to_ret = []
        subset = []

        def recur(i):
            
            if i >= len(nums):
                to_ret.append(subset.copy())
                return
            subset.append(nums[i])
            recur(i+1)
            subset.pop()
            recur(i+1)
        recur(0)
        return to_ret
