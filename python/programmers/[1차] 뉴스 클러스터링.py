from math import floor
def solution(str1, str2):
    answer = 0

    str1_list = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2_list = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    cha_list = set(str1_list) & set(str2_list)
    hap_list = set(str1_list) | set(str2_list)
    
    if len(cha_list)==0 and len(hap_list) ==0:
        return 65536
    
    cha_sum = sum([min(str1_list.count(a),str2_list.count(a)) for a in cha_list])
    hap_sum = sum([max(str1_list.count(b),str2_list.count(b)) for b in hap_list])
    
    return floor((cha_sum/hap_sum)*65536)