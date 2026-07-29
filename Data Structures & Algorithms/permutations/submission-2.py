class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        permutations = self.permute(nums[1:])
        to_ret = []
        for perm in permutations:
            for i in range(len(perm) + 1):
                new = perm.copy()
                new.insert(i, nums[0])
                to_ret.append(new)
        return to_ret