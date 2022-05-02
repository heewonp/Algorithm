from itertools import permutations
from collections import deque

def cal(a,b,op):
    if op == '*':
        return str(int(a) * int(b))
    elif op == '-':
        return str(int(a) - int(b))
    elif op == '+':
        return str(int(a) + int(b))

def make_res(exp,op):
    arr = deque()
    num = ''
    for i in exp:
        if i.isdigit():
            num += i
        else:
            arr.append(num)
            arr.append(i)
            num = ''
            
    arr.append(num)
    
    for o in op:
        stack = []
        while len(arr) != 0:
            temp = arr.popleft()
            if temp == o:
                stack.append(cal(stack.pop(),arr.popleft(),o))
            else:
                stack.append(temp)
        arr = deque(stack)
    return abs(int(arr.pop()))
            
    
def solution(expression):
    answer = 0
    op = ['*','-','+']
    for i in list(permutations(op,3)):
        answer = max(answer,make_res(expression,i))
    return answer