import sys
input = sys.stdin.readline

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a
        number[a] += number[b]
        
for _ in range(int(input())):
    num = int(input())
    parent,number = {},{}
    for i in range(num):
        x,y = input().split()
        
        if x not in parent:
            parent[x] = x
            number[x] = 1
            
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union(x,y)
        print(number[find(x)])