def solution(x):
    x_sum = sum(map(int,str(x)))
    
    if x % x_sum == 0:
        return True
    else:
        return False