class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #State of asteroids after all collisions
        #Two meet, small explode
        #equal size both explode
        #Same dirs never meet

        travel_r = []

        to_ret = []

        for i in asteroids:
            if i > 0:
                #To the right
                travel_r.append(i)
            elif i < 0:
                killed = False
                while travel_r and not killed:
                    if abs(i) > travel_r[-1]:
                        travel_r.pop()
                    elif abs(i) == travel_r[-1]:
                        travel_r.pop()
                        killed = True           
                    else:
                        killed = True
                if not killed:
                    to_ret.append(i)
        return to_ret + travel_r