from itertools import permutations

def check(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
def solution(numbers):
        
    num = [i for i in numbers]
    per = []
    answer = 0
    
    for i in range(1,len(numbers)+1):
        per += list(permutations(num,i))
    
    arr_per = set([int(('').join(j)) for j in per])
    
    for n in arr_per:
        if check(n):
            answer += 1
    return answer
        