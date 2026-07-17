class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        to_ret = []
        subset = []
        nums.sort()

        def recur(i):
            if i >= len(nums):
                to_ret.append(subset.copy())
                return
            subset.append(nums[i])
            recur(i+1)
            while i + 1< len(nums) and nums[i] == nums[i+1]:
                i += 1
            subset.pop()
            recur(i + 1)
        recur(0)

        return to_ret