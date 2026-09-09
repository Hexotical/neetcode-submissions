class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        check = 0
        to_ret = len(nums) + 1
        while r < len(nums):
            check += nums[r]
            while check >= target and l <= r:
                to_ret = min(to_ret, r-l + 1)
                check -= nums[l]
                l += 1
            r += 1
        if to_ret == len(nums) + 1:
            return 0
        return to_ret
            