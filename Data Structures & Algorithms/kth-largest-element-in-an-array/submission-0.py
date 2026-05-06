class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        #kth largest is len - k smallest
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return nums[0]
        