class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #So the obvious way to me at least
        #count the 3 dif elems
        #rewrite after doing a ocunt
        #They have a 2 pointer approach
        #I assume one at each end
        l = 0
        r = len(nums)-1
        cur = 0
        while cur <= r:
            if nums[cur] == 0:
                nums[l], nums[cur] = nums[cur], nums[l]
                l += 1
            elif nums[cur] == 2:
                nums[r], nums[cur] = nums[cur], nums[r]
                r -= 1
                cur -= 1
            
            cur += 1
