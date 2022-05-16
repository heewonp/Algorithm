from itertools import product
def solution(word):
    answer = []
    alpas = ['A','E','I','O','U']
             
    for i in range(6):
        for j in product(alpas,repeat=i):
            answer.append(''.join(list(j)))
    
    answer = sorted(answer)
    
    return answer.index(word)