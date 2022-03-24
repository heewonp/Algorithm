def solution(id_list, report, k):
    answer = []
    id_dic ={name:[] for i,name in enumerate(id_list)}
    report_dic = {name:0 for i,name in enumerate(id_list)}
    
    for i in set(report):
        user_id, report_id = i.split()
        id_dic[user_id].append(report_id)
        report_dic[report_id] += 1
    
    answer = [0 for i in range(len(id_list))]
    for key,value in id_dic.items():
        for val in value:
            if report_dic[val] >= k:
                answer[id_list.index(key)] += 1
    return answer