class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #Nums may contain duplicates
        #unique permutations
        if not nums:
            return [[]]
        to_ret = set()
        perms = self.permuteUnique(nums[1:])
        for p in perms:
            for i in range(len(p)+1):
                to_add = p.copy()
                
                to_add.insert(i, nums[0])
                to_ret.add(tuple(to_add))
        return [list(x) for x in to_ret]
        