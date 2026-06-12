class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #a, b, c, d such that the numbers are distinct
        #a + b + c + d== target
        if len(nums) < 4:
            return []
        nums.sort()
        a = 0
        b = 1
        c = len(nums) - 2
        d = len(nums) - 1
        to_ret = set()
        while a < len(nums)-3:
            d = len(nums) - 1
            
            while d - a >= 3:
                b = a + 1
                c = d - 1
                while b < c:
                    running_total = nums[a] + nums[b] + nums[c] + nums[d]
                    if running_total == target:
                        to_ret.add((nums[a], nums[b], nums[c], nums[d]))
                        
                        b += 1
                    elif running_total < target:
                        b += 1
                        while b < c and nums[b] == nums[b - 1]:
                            b += 1
                    elif running_total > target:
                        c -= 1
                        while b < c and nums[c] == nums[c + 1]:
                            c -= 1
                d -= 1
                    
            a += 1
        
        return [list(x) for x in to_ret]