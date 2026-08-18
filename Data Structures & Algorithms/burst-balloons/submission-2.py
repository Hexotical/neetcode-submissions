class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = dict()
        def helper(l, r):
            if (l, r) in memo:
                return memo[(l,r)]
            to_ret = 0
            for i in range(l, r + 1):
                to_ret = max(to_ret,  nums[i] * nums[l-1] * nums[r+1] + helper(l, i-1) + helper(i+1, r))
            memo[(l, r)] = to_ret
            return to_ret

        return helper(1, len(nums) - 2)