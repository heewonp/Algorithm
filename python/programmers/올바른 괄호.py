def solution(s):
    answer = []
    for i in s:
        if i == '(':
            answer.append(i)
        else:
            if len(answer) == 0:
                return False
            else:
                answer.pop()
            
        
    return len(answer) == 0