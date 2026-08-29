class Solution:
    def candy(self, ratings: List[int]) -> int:
        #Start from valleys and expand out
        if len(ratings) == 1:
            return 1

        valleys = []
        if ratings[0] <= ratings[1]:
            valleys.append(0)
        for i in range(1, len(ratings)-1):
            if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                valleys.append(i)
        candies = [1] * len(ratings)
        
        if ratings[-1] <= ratings[-2]:
            valleys.append(len(ratings) - 1)
        visited = set()
        while valleys:
            index = valleys.pop()
            candies[index] = 1
            l = index - 1
            #print(index)
            while l >= 0 and ratings[l] > ratings[l+1]:
                
                candies[l] = max(candies[l], candies[l+1] + 1)
                l -= 1
            #print(l)
            r = index + 1
            while r < len(ratings) and ratings[r] > ratings[r-1]:
                candies[r] = max(candies[r], candies[r-1] + 1)
                r += 1
            #print(r)
        #print(candies)
                
        return sum(candies)