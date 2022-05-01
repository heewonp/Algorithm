from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    
    for i in course:
        temp = []
        for j in orders:
            menu = combinations(sorted(j),i)
            temp += menu
        menu_cnt = Counter(temp)
        
        if menu_cnt:
            if max(menu_cnt.values()) >= 2:
                for key,value in menu_cnt.items():
                    if value == max(menu_cnt.values()):
                        answer.append(''.join(key))
    return sorted(answer)