import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) # 최대 재귀함수 깊이 설정 해주지 않으면 런타임에러 발생
n = int(input())
m = int(input())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

for y in range(1,n+1):
    maps = list(map(int,input().split()))
    for x in range(1,len(maps)+1):
        if maps[x-1] == 1:
            union(y,x)

tour = list(map(int,input().split()))
res = set([find(i) for i in tour])

if len(res) != 1:
    print('NO')
else:
    print('YES')