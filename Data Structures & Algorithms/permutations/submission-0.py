class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #Unique integers
        #all possible permutations
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                to_add = p.copy()
                to_add.insert(i, nums[0])
                res.append(to_add)
        return res