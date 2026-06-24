class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Subarray largest prodcut 
        #Return the product
        #So the brute force way is just go through
        #Every single subarray
        #Which is n^2 time complexity
        #linear time constant space??
        to_ret = nums[0]
        cur_max, cur_min = 1, 1
        for i in nums:
            temp = cur_max * i
            cur_max = max(i, temp, cur_min*i)
            cur_min = min(i, temp, cur_min*i)
            to_ret = max(cur_max, to_ret)
        return to_ret