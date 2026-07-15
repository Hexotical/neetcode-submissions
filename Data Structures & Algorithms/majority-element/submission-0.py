class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Fun voting algorithm
        count = 1
        elem = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == elem:
                count += 1
            else:
                count -= 1
            if count < 0:
                elem = nums[i]
                count = 1
        return elem