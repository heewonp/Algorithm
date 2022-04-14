def solution(lottos, win_nums):
    answer = [6,6,5,4,3,2,1]
    zeros = lottos.count(0)
    cnt = 0
    
    for i in lottos:
        if i in win_nums:
            cnt += 1
    
    return answer[zeros+cnt],answer[cnt]