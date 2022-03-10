def solution(participant, completion):
    temp = {}
    for part in participant:
        if part not in temp.keys():
            temp[part]= 0
        temp[part] += 1
    for com in completion:
        temp[com] -= 1
    for k in temp.keys():
        if temp[k] ==1:
            return k