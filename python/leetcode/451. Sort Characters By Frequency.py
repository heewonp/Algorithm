import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        
        cnt = {}
        
        for i in s:
            if i in cnt :
                cnt[i] += 1
            else:
                cnt[i] = 1
        
        heap = []
        
        for key,value in cnt.items():
            heapq.heappush(heap,(-value,key))
        
        res = ''
        
        while heap:
            value, key = heapq.heappop(heap)
            
            res += key*(-value)
                
        return res