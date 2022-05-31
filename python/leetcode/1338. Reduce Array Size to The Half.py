from collections import Counter
import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        cnt_arr = Counter(arr)
        heap = []
        
        for key,value in cnt_arr.items():
             heapq.heappush(heap, (-value, key))
                
        
        cnt = 0
        size = len(arr)
        
        while heap and size > 0:
            value,key = heapq.heappop(heap)
            size -= -value
            cnt += 1
            
            if size <= len(arr)/2:
                return cnt
            
  

        
        
            
            
        