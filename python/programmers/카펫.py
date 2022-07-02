def solution(brown, yellow):
    answer = []
    
    all = brown + yellow
    for b in range(3,brown//2):
        if (b-2) *(brown//2-b) == yellow:

            return [brown//2-b+2,b]