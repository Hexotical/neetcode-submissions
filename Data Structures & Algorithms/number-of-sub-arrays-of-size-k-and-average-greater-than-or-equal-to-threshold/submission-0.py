class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #num sub arrays size k
        #Avg greater equl to threshold
        #subarray is contigous
        #Sliding window??
        total = 0
        for i in range(k):
            total += arr[i]
        l = 0
        r = k - 1
        to_ret = 0
        while r < len(arr):
            if (total / k) >= threshold:
                #print(l, r)
                to_ret += 1
            total -= arr[l]
            l += 1
            if r +1 < len(arr):
                total += arr[r+1]
            r += 1
        return to_ret
            
