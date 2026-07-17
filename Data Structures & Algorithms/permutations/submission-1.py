class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        perms = self.permute(nums[1:])
        to_ret = []
        for p in perms:
            for i in range(len(p) + 1):
                new = p.copy()
                new.insert(i, nums[0])
                to_ret.append(new)
        return to_ret
