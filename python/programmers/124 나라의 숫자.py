def solution(n):
    answer = ''
    num_arr = ['1','2','4']
    while n>0:
        n-=1
        answer = num_arr[n%3] + answer
        n //= 3
        
    return answer