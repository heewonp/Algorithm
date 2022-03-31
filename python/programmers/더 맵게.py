import heapq
def solution(scoville, K):
    mix_cnt = 0
    heapq.heapify(scoville)
    
    while scoville[0]< K :
        if len(scoville)>1:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) *2)
            mix_cnt +=1
        else:
            return -1
        
    return mix_cnt