def solution(answers):
    pat1 = [1,2,3,4,5]
    pat2 = [2,1,2,3,2,4,2,5]
    pat3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]
    answer = []
    
    for idx,x in enumerate(answers):
        if x == pat1[idx%len(pat1)]:
            score[0] += 1
        if x == pat2[idx%len(pat2)]:
            score[1] += 1
        if x == pat3[idx%len(pat3)]:
            score[2] += 1
            
    for idx,i in enumerate(score):
        if i == max(score):
            answer.append(idx+1)
    
    return answer