def solution(priorities, location):
    answer = 0
    temp = [(i,x) for x,i in enumerate(priorities)]
    
    
    while temp:
        a = temp.pop(0)
        if temp and max(temp)[0] > a[0]:
            temp.append(a)
        else:
            answer +=1
            
            if a[1] == location:
                break
            
    return answer