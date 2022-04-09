import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        heap_num = sorted(heapq.nlargest(k, nums))
        
        return heap_num[0]