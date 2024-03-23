class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-nums for nums in nums]
        heapq.heapify(nums)
        for x in range(k):
            k=heapq.heappop(nums)
        return -k