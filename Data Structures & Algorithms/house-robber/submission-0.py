class Solution:
    def rob(self, nums: List[int]) -> int:
        #Maximum amount of money without alerting the police
        #Can't rob an adjacent house
        if len(nums) <=2 :
            return max(nums)

        max_money = [0] * len(nums)
        max_money[0] = nums[0]
        max_money[1] = nums[1]
        max_money[2] = max(nums[2], nums[0] + nums[2])


        for i in range(3, len(nums)):
            max_money[i] = max(nums[i], nums[i] + max_money[i-2], nums[i] + max_money[i-3])
            
        return max(max_money[-2], max_money[-1], max_money[-3])
            