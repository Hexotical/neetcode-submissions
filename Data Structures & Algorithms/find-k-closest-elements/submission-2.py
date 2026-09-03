class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-1
        
        mid = None
        while l<=r:
            mid = l + (r-l)//2
            if arr[mid] == x:
                break
            elif arr[mid] > x:
                r = mid-1
            else:
                l = mid+1
        #print(mid)
        if k == len(arr):
            return arr
        print(mid)
        if arr[mid] != x:
            if mid < len(arr) - 1:
                if abs(arr[mid+1] - x) < abs(arr[mid] - x):
                    mid += 1
            if abs(arr[mid-1] - x) <= abs(arr[mid] - x ):
                mid -= 1 
        
        #So mid is out closest elem
        left = mid
        right = mid + 1
        while len(arr[left:right]) < k:
            if left == 0:
                right += 1
            elif right == len(arr):
                left -= 1
            elif abs(arr[left-1] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        return arr[left:right]
            

        
