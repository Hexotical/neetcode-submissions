class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        to_ret = set()


        combo = []

        def dfs(i, run_sum):
            if run_sum == target:
                to_ret.add(tuple(combo))
                return
            if i >= len(candidates) or run_sum > target:
                return
            run_sum += candidates[i]
            combo.append(candidates[i])

            dfs(i + 1, run_sum)
            run_sum -= candidates[i]
            combo.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, run_sum)


        dfs(0, 0)
        to_ret = [list(x) for x in to_ret]
        return to_ret