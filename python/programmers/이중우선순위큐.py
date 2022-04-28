import heapq
def solution(operations):
    answer = []
    for i in operations:
        sign,num = i.split(' ')
        if sign == 'I':
            heapq.heappush(answer,int(num))
        else:
            if len(answer) > 0:
                if num == '1':
                    answer.pop(answer.index(heapq.nlargest(1,answer)[0]))
                else:
                    heapq.heappop(answer)
                    
    if len(answer) == 0:
        return [0,0]
    else:
        return [heapq.nlargest(1,answer)[0],heapq.nsmallest(1,answer)[0]]