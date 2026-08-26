class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Range from 0 to n
        #I think there's a way to do this w/dfs
        #pretend it's a graph use dfs
        #how do i use bit manip
        to_ret = 0
        for i in range(len(nums)+1):
            to_ret = to_ret ^ i
        for j in nums:
            to_ret = to_ret ^ j
        return to_ret