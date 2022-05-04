def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        temp_answer = ''
        temp = s[:i]
        cnt = 1
        
        for j in range(i,len(s)+i,i):
            if temp == s[j:i+j]:
                cnt +=1
            else:
                if cnt == 1:
                    temp_answer += temp
                else:
                    temp_answer += str(cnt)+temp
                temp = s[j: j+i]
                cnt = 1
        answer = min(answer,len(temp_answer))
    return answer