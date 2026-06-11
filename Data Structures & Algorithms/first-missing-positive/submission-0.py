class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #smallest positive integer not present in nums
        #Linear time
        #constant space
        #Sorting is nlogn time
        #n is isze of nums

        #I probably do just hate myself
        #Anyway
        #Oh i get ittttt
        for i, v in enumerate(nums):
            if v <= 0:
                nums[i] = 0
        
        for i, v in enumerate(nums):
            v = abs(v)
            if 0 < v <= len(nums):
                if nums[v-1] == 0:
                    nums[v-1] = -1 * (len(nums)+1)
                elif nums[v-1] > 0:
                    nums[v-1] *= -1
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0:
                return i
        return len(nums) + 1

