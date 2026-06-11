class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Linear time, constant extra space
        #Sum the array?
        res = 0
        for num in nums:
            res = num ^ res
        return res