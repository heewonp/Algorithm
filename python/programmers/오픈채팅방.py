def solution(record):
    answer = []
    nick_dic = {}
    for i in record:
        id = i.split()
        if len(id) == 3:
            nick_dic[id[1]] = id[2]
    
    for j in record:
        act = j.split()
        if act[0] == "Enter":
            answer.append(f"{nick_dic[act[1]]}님이 들어왔습니다.")
        elif act[0] == "Leave":
            answer.append(f"{nick_dic[act[1]]}님이 나갔습니다.")