# 1번 
def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        cnt = 0
        for j in range(i,len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                cnt +=1
        answer.append(cnt)
    return answer


# 큐 이용
from collections import deque

def solution(prices):
    answer = []
    
    q_prices = deque(prices)
    
    while q_prices:
        p = q_prices.popleft()
        sec = 0
        
        for i in q_prices:
            sec +=1
            if i < p:
                break
                
        answer.append(sec)
    
    return answer