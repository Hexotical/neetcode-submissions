class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        #Making a square from matchsticks
        #So it's going to have to be at least 
        #It's a squaree
        total_matchsticks = sum(matchsticks)
        length = total_matchsticks / 4

        if total_matchsticks % 4 != 0:
            return False
        #Need to find valid divisions
        matchsticks.sort(reverse=True)

        sides = [0, 0, 0, 0]

        def dfs(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            for side in range(4):
                if sides[side] + matchsticks[i] <= length: 
                    sides[side] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[side] -= matchsticks[i]
            return False
        return dfs(0)