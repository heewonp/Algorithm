def solution(N, stages):
    fail_score = {}
    length = len(stages)
    
    for i in range(1,N+1):
        if length != 0:
            cnt = stages.count(i)
            fail_score[i] = cnt/length
            length -= cnt
        else:
            fail_score[i] = 0
    
    return sorted(fail_score, key = lambda x : fail_score[x],reverse=True)
            