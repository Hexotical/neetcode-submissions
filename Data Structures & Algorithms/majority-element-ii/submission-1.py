class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #Linear time, constant space
        #because easy otherwise
        can1 = None
        count1 = 0
        can2 = None
        count2 = 0
        for i in nums:
            if i == can1:
                count1 += 1
            elif i == can2:
                count2 += 1
            else:
                if count2 == 0:
                    can2 = i
                    count2 = 1
                elif count1 == 0:
                    can1 = i
                    count1 = 1
                else:
                    count1 -= 1
                    count2 -= 1
                    
        c1 = 0
        c2 = 0
        for i in nums:
            if i == can1:
                c1 += 1
            elif i == can2:
                c2 += 1
        print(can1, can2)
        if c1 > len(nums)//3 and c2 > len(nums)//3:
            return [can1, can2]
        elif c1 > len(nums)//3:
            return [can1]
        elif c2 > len(nums)//3:
            return [can2]
        return []
        