class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #Two baskets
        #Must pick a fruit
        #SLiding window?
        to_ret = 0
        cur_window = 0
        left = right = 0
        window = dict()
        while right < len(fruits):
            if fruits[right] not in window:
                window[fruits[right]] = 1
            else:
                window[fruits[right]] += 1
            cur_window += 1
            while len(window.keys()) > 2:
                window[fruits[left]] -= 1
                cur_window -= 1
                if window[fruits[left]] == 0:
                    window.pop(fruits[left])
                left += 1
            #print(cur_window)
            #print(window)
            to_ret = max(to_ret, cur_window)
            right += 1
        
        return to_ret