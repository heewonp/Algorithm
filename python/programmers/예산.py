def solution(d, budget):
    d = sorted(d)
    
    while budget < sum(d):
        d.pop()
        
    return len(d)