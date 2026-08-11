class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Try to do this bottom up
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2
        candidates = set()
        candidates.add(0)
        for i in nums:
            to_add = set()
            for j in candidates:
                temp = i + j
                if temp > target:
                    continue
                elif temp == target:
                    return True
                else:
                    to_add.add(temp)
            candidates |= to_add
            if i < target:
                candidates.add(i)

        return False