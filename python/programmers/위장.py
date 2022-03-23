def solution(clothes):
    clothes_dic ={}
    for cloth,types in clothes:
        if types in clothes_dic:
            clothes_dic[types] += 1
        else:
            clothes_dic[types] = 1

    answer = 1
    for value in clothes_dic.values():
        answer *= (value+1)
        
    return answer-1