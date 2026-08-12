class Solution:
    def rob(self, nums: List[int]) -> int:
        #Top down
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def dfs(i, first):
            if (i, first) in memo:
                return memo[(i, first)]
            if i >= len(nums):
                return 0
            if first and i == len(nums) - 1:
                return 0
            elif not first and i == len(nums) - 1:
                return nums[-1]
            memo[(i, first)] = max(nums[i] + dfs(i+2, first), dfs(i+1, first))
            return memo[(i, first)]
            


        first_house = dfs(0, True)
        second_house = dfs(1, False)
        return max(first_house, second_house)
        