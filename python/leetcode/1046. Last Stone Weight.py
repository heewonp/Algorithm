import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap_stone = [-i for i in stones]
        heapq.heapify(heap_stone)
        
        while len(heap_stone) > 1:
            s_1 = heapq.heappop(heap_stone)
            s_2 = heapq.heappop(heap_stone)
            
            if s_1 != s_2:
                heapq.heappush(heap_stone, s_1-s_2)
            
        if len(heap_stone): 
            return -heap_stone[0]
        else:
            return 0     
        